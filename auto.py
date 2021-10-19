{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red74\green74\blue74;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid1\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl336\partightenfactor0
\ls1\ilvl0
\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u1060 \u1091 \u1085 \u1082 \u1094 \u1080 \u1103 , \u1082 \u1086 \u1090 \u1086 \u1088 \u1072 \u1103  \u1086 \u1073 \u1088 \u1072 \u1097 \u1072 \u1077 \u1090  \u1074 \u1089 \u1077  \u1089 \u1090 \u1088 \u1086 \u1082 \u1080  \u1074  \u1095 \u1080 \u1089 \u1083 \u1072  \u1080  \u1087 \u1086 \u1076 \u1089 \u1090 \u1072 \u1074 \u1083 \u1103 \u1077 \u1090  \u1079 \u1085 \u1072 \u1095 \u1077 \u1085 \u1080 \u1077  \u1087 \u1086  \u1091 \u1084 \u1086 \u1083 \u1095 \u1072 \u1085 \u1080 \u1102 , \u1077 \u1089 \u1083 \u1080  \u1074 \u1089 \u1090 \u1088 \u1077 \u1095 \u1072 \u1077 \u1090  \u1087 \u1088 \u1086 \u1087 \u1091 \u1089 \u1082 .  \
def digitize_values(collection, default=0):  \
    no_missed = [value if value else default for value in collection]   \
    return [float(value) for value in no_missed]  \
  \
# \uc0\u1052 \u1099  \u1087 \u1077 \u1088 \u1077 \u1076 \u1072 \u1105 \u1084  \u1085 \u1072  \u1074 \u1093 \u1086 \u1076  \u1087 \u1088 \u1086 \u1080 \u1079 \u1074 \u1086 \u1083 \u1100 \u1085 \u1099 \u1077  \u1087 \u1072 \u1088 \u1072 \u1084 \u1077 \u1090 \u1088 \u1099  \u1080  \u1089 \u1084 \u1086 \u1090 \u1088 \u1080 \u1084 , \u1095 \u1090 \u1086  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1103  \u1082 \u1086 \u1088 \u1088 \u1077 \u1082 \u1090 \u1085 \u1086  \u1088 \u1072 \u1073 \u1086 \u1090 \u1072 \u1077 \u1090  \u1089  \u1085 \u1080 \u1084 \u1080    \
# \uc0\u1055 \u1088 \u1086 \u1074 \u1077 \u1088 \u1080 \u1084 , \u1095 \u1090 \u1086  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1103  \u1082 \u1086 \u1088 \u1088 \u1077 \u1082 \u1090 \u1085 \u1086  \u1086 \u1073 \u1088 \u1072 \u1097 \u1072 \u1077 \u1090  \u1089 \u1087 \u1080 \u1089 \u1086 \u1082  \u1089 \u1090 \u1088 \u1086 \u1082  \u1074  \u1089 \u1087 \u1080 \u1089 \u1086 \u1082  \u1095 \u1080 \u1089 \u1077 \u1083   \
def test_digitize_convert_to_float():  \
    assert digitize_values(["10", "50"])  == [10, 50]  \
    assert digitize_values(["70.2", "33.4"]) == [70.2, 33.4]  \
      \
# \uc0\u1061 \u1086 \u1088 \u1086 \u1096 \u1077 \u1081  \u1087 \u1088 \u1072 \u1082 \u1090 \u1080 \u1082 \u1086 \u1081  \u1089 \u1095 \u1080 \u1090 \u1072 \u1077 \u1090 \u1089 \u1103  \u1087 \u1086 \u1082 \u1088 \u1099 \u1074 \u1072 \u1090 \u1100  \u1088 \u1072 \u1079 \u1085 \u1099 \u1077  \u1072 \u1089 \u1087 \u1077 \u1082 \u1090 \u1099  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1080  \u1074  \u1088 \u1072 \u1079 \u1085 \u1099 \u1093  \u1090 \u1077 \u1089 \u1090 \u1072 \u1093   \
# \uc0\u1047 \u1076 \u1077 \u1089 \u1100  \u1084 \u1099  \u1087 \u1088 \u1086 \u1074 \u1077 \u1088 \u1080 \u1084 , \u1095 \u1090 \u1086  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1103  \u1079 \u1072 \u1082 \u1088 \u1099 \u1074 \u1072 \u1077 \u1090  \u1087 \u1088 \u1086 \u1087 \u1091 \u1089 \u1082 \u1080    \
def test_digitize_restore_missed():  \
    assert digitize_values([""], 10) == [10]  \
    assert digitize_values(["20", None], 50) == [20, 50]  \
      \
# \uc0\u1045 \u1097 \u1105  \u1089 \u1090 \u1086 \u1080 \u1090  \u1087 \u1088 \u1086 \u1074 \u1077 \u1088 \u1103 \u1090 \u1100 , \u1095 \u1090 \u1086  \u1085 \u1072 \u1096 \u1072  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1103  \u1082 \u1086 \u1088 \u1088 \u1077 \u1082 \u1090 \u1085 \u1086  \u1088 \u1072 \u1073 \u1086 \u1090 \u1072 \u1077 \u1090  \u1085 \u1072  \u1075 \u1088 \u1072 \u1085 \u1080 \u1095 \u1085 \u1099 \u1093  \u1079 \u1085 \u1072 \u1095 \u1077 \u1085 \u1080 \u1103 \u1093   \
# \uc0\u1053 \u1072 \u1087 \u1088 \u1080 \u1084 \u1077 \u1088 , \u1085 \u1072  \u1087 \u1091 \u1089 \u1090 \u1099 \u1093  \u1076 \u1072 \u1085 \u1085 \u1099 \u1093   \
def test_digitize_empty():  \
    assert digitize_values([]) == []}