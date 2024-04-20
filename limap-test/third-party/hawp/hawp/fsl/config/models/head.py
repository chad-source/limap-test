from yacs.config import CfgNode as CN

PARSING_HEAD = CN()

PARSING_HEAD.MAX_DISTANCE = 5.0

PARSING_HEAD.N_STC_POSL = 300
PARSING_HEAD.N_STC_NEGL = 40

PARSING_HEAD.MATCHING_STRATEGY = 'junction' #junction or line_adjusted
PARSING_HEAD.N_DYN_JUNC = 300
PARSING_HEAD.N_DYN_POSL = 300
PARSING_HEAD.N_DYN_NEGL = 300
PARSING_HEAD.N_DYN_OTHR = 0
PARSING_HEAD.N_DYN_OTHR2 = 300

PARSING_HEAD.N_PTS0 = 32
PARSING_HEAD.N_PTS1 = 8

PARSING_HEAD.DIM_LOI = 128
PARSING_HEAD.DIM_FC  = 1024
PARSING_HEAD.USE_RESIDUAL = 1
PARSING_HEAD.N_OUT_JUNC = 250
PARSING_HEAD.N_OUT_LINE = 2500
PARSING_HEAD.JMATCH_THRESHOLD = 1.5
PARSING_HEAD.J2L_THRESHOLD = 1000.0
#INFERENCE FLAGS
#0, only use junctions to yield line segments
#1, only use learned angles to yield line segments
#2, match line segment proposals with junctions
# PARSING_HEAD.INFERENCE = 0