#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vim
from clap.scorer import fzy_scorer, substr_scorer


def str2bool(v):
    #  For neovim, vim.eval("a:enable_icon") is str
    #  For vim, vim.eval("a:enable_icon") is bool
    return v if isinstance(v, bool) else v.lower() in ("yes", "true", "t", "1")


def apply_score(scorer, query, candidates, enable_icon):
    scored = []

    for c in candidates:
        #  Skip two chars
        candidate = c[2:] if enable_icon else c
        score, indices = scorer(query, candidate)
        if score != float("-inf"):
            if enable_icon:
                indices = [x + 4 for x in indices]
            scored.append({'score': score, 'indices': indices, 'text': c})

    return scored


def fuzzy_match_py(query, candidates, enable_icon):
    scorer = substr_scorer if ' ' in query else fzy_scorer
    scored = apply_score(scorer, query, candidates, enable_icon)
    ranked = sorted(scored, key=lambda x: x['score'], reverse=True)

    indices = []
    filtered = []
    for r in ranked:
        filtered.append(r['text'])
        indices.append(r['indices'])

    return (indices, filtered)


def clap_fzy_py():
    return fuzzy_match_py(vim.eval("a:query"), vim.eval("a:candidates"),
                          str2bool(vim.eval("a:context")['enable_icon']))


try:
    from clap.fuzzymatch_rs import fuzzy_match as fuzzy_match_rs

    def clap_fzy_rs():
        return fuzzy_match_rs(vim.eval("a:query"), vim.eval("a:candidates"),
                              vim.eval("a:recent_files"),
                              vim.eval("a:context"))
except Exception:
    pass
