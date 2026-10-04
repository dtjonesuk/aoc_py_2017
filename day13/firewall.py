from pyparsing import *

LAYER = pyparsing_common.integer.set_results_name('layer')
DEPTH = pyparsing_common.integer.set_results_name('depth')
SEP = Suppress(":")
EXPR = LAYER + SEP + DEPTH

def parse_line(s:str):
    expr = EXPR.parse_string(s)
    return expr.layer, expr.depth

