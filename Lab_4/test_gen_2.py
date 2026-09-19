
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BASE TEST CASE:
sex:F age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DEFINE TEST CASE "STRUCT"
in Python, the closest thing to a struct is a dataclass
i wish i'd done this in C++ ): *cries*
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from dataclasses import dataclass
from copy import copy

@dataclass
class test_case:
    sex: str
    age: int
    cho: int
    smo: str
    hdl: int
    sbp: int
    med: str
    out: str

    def __str__(self):
        return (
            f"sex:{self.sex} "
            f"age:{self.age} "
            f"cho:{self.cho} "
            f"smo:{self.smo} "
            f"hdl:{self.hdl} "
            f"sbp:{self.sbp} "
            f"med:{self.med} "
            f"out:{self.out}\n"
        )
# I take back my hate, having a to_string() method on a 
# struct is kinda groovy

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
POINT VALUE TABLES:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

points_sex_age = [
    # F
    [-7, -3, 0, 3, 6, 8, 10, 12, 14, 16],
    # M
    [-9, -4, 0, 3, 6, 8, 10, 11, 12, 13]
]

points_sex_cho_age = [
    # F
    [
    #   20-39   40-49   50-59   60-69   70-79
        [0,     0,      0,      0,      0],     # <160
        [4,     3,      2,      1,      1],     # 160-199
        [8,     6,      4,      2,      1],     # 200-239
        [11,    8,      5,      3,      2],     # 240-279
        [13,    10,     7,      4,      2]      # >=280
    ],
    # M
    [
    #   20-39   40-49   50-59   60-69   70-79
        [0,     0,      0,      0,      0],     # <160
        [4,     3,      2,      1,      0],     # 160-199
        [7,     5,      3,      1,      0],     # 200-239
        [9,     6,      4,      2,      1],     # 240-279
        [11,    8,      5,      3,      1]      # >=280
    ]
]

points_sex_smo_age = [
    # F
    [
    #   20-39   40-49   50-59   60-69   70-79
        [0,     0,      0,      0,      0],     # N
        [9,     7,      4,      2,      1]      # Y
    ],
    # M
    [ 
    #   20-39   40-49   50-59   60-69   70-79
        [0,     0,      0,      0,      0],     # N
        [8,     5,      3,      1,      1]      # Y
    ]
]

points_hdl = [
    -1, # >=60
     0, # 50-59
     1, # 40-49
     2  # <40
]

points_sex_sbp_med = [
    # F
    [
    #   N   Y
        [0, 0],     # <120
        [1, 3],     # 120-129
        [2, 4],     # 130-139
        [3, 5],     # 140-159
        [4, 6]      # >=160
    ],
    # M
    [
    #   N   Y
        [0, 0],     # <120
        [0, 1],     # 120-129
        [1, 2],     # 130-139
        [1, 2],     # 140-159
        [2, 3]      # >=160
    ],
]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
TEST RANGES
    [l_bound, mid_val, r_bound], # Representative Range
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# WHY ARE THERE NO REGULAR OL' ENUMS IN PYTHONNNN
L_BOUND = 0
MID_VAL = 1
R_BOUND = 2

test_age_10 = [
    [20,    27,     34],    # 20-34
    [35,    37,     39],    # 35-39
    [40,    42,     44],    # 40-44
    [45,    47,     49],    # 45-49
    [50,    52,     54],    # 50-54
    [55,    57,     59],    # 55-59
    [60,    62,     64],    # 60-64
    [65,    67,     69],    # 65-69
    [70,    72,     74],    # 70-74
    [75,    77,     79]     # 75-79
]

test_age_5 = [
    [20,    30,     39],    # 20-39
    [40,    45,     49],    # 40-49
    [50,    55,     59],    # 50-59
    [60,    65,     69],    # 60-69
    [70,    75,     79]     # 70-79
]

test_cho = [
    [0,     120,    159],   # <160
    [160,   180,    199],   # 160-199
    [200,   220,    239],   # 200-239
    [240,   260,    279],   # 240-279
    [280,   300,    999]    # >=280
]

test_hdl = [
    [60,    70,     999],   # >=60
    [50,    55,     59],    # 50-59
    [40,    45,     49],    # 40-49
    [0,     30,     39]     # <40
]

test_sbp = [
    [0,     100,    119],   # <120
    [120,   125,    129],   # 120-129
    [130,   135,    139],   # 130-139
    [140,   150,    159],   # 140-159
    [160,   180,    999]    # >=160
]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
TEST BOOLEANS [0, 1]
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

test_sex = ['F', 'M']
test_smo = ['N', 'Y']
test_med = ['N', 'Y']

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
MAP RANGES TO INDEX
    Map value to correct range and return its index in the 
    table. For ranged values such as:
        age
        cho
        sbp
        hald
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def range_i(value, range_bounds):
    i = 0
    for range in range_bounds:
        if (range[L_BOUND] <= value <= range[R_BOUND]):
            return i
        else: 
            i += 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
MAP BOOL TO INDEX
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def bool_i(value):
    match(value):
        case 'F' | 'N': return 0
        case 'M' | 'Y': return 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
MAP POINTS OUTPUT TO FINAL RISK SCORE
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

POINTS_TOT = 0
RISK_PERCENT = 1

point_risk_ranges = [
    # F
    [
        [-999,  '<1'],  # <9
        [9,     '1'],
        [10,    '1'],
        [11,    '1'],
        [12,    '1'],
        [13,    '2'],
        [14,    '2'],
        [15,    '3'],
        [16,    '4'],
        [17,    '5'],
        [18,    '6'],
        [19,    '8'],
        [20,    '11'],
        [21,    '14'],
        [22,    '17'],
        [23,    '22'],
        [24,    '27'],
        [25,    '>30']  # >=25
    ],
    # M
    [
        [-999,  '<1'],  # <0
        [0,     '1'],
        [1,     '1'],
        [2,     '1'],
        [3,     '1'],
        [4,     '1'],
        [5,     '2'],
        [6,     '2'],
        [7,     '3'],
        [8,     '4'],
        [9,     '5'],
        [10,    '6'],
        [11,    '8'],
        [12,    '10'],
        [13,    '12'],
        [14,    '16'],
        [15,    '20'],
        [16,    '25'],
        [17,    '>30']  # >=17
    ]
]

def points_to_risk(sex: bool, points: int):
    for range in reversed(point_risk_ranges[sex]):
        if points >= range[POINTS_TOT]:
            return range[RISK_PERCENT]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
CALC TEST OUTPUT FUNCTION
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def calc_out(t: test_case):
    sex = bool_i(t.sex)
    age10 = range_i(t.age, test_age_10)
    age5 = range_i(t.age, test_age_5)
    cho = range_i(t.cho, test_cho)
    smo = bool_i(t.smo)
    hdl = range_i(t.hdl, test_hdl)
    sbp = range_i(t.sbp, test_sbp)
    med = bool_i(t.med)
    points = (
        points_sex_age[sex][age10] +
        points_sex_cho_age[sex][cho][age5] +
        points_sex_smo_age[sex][smo][age5] +
        points_hdl[hdl] +
        points_sex_sbp_med[sex][sbp][med]
    )
    return points_to_risk(sex, points)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
MAIN: GENERATE TESTS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def main():
    with open("tyr_test_cases.txt", 'w') as out:
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        BASE TEST CASE:
        sex:F age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        base_case = test_case(
            sex='F',
            age=40,
            cho=105,
            smo='N',
            hdl=60,
            sbp=100,
            med='N',
            out='undef'
        )
        case = copy(base_case)

        # TABLE: Age
        # points_sex_age
        for sex in test_sex:
            case.sex = sex
            # Lower Corner Case
            case.age = test_age_10[0][L_BOUND]
            case.out = calc_out(case)
            out.write(str(case))
            for age_range in test_age_10:
                # Middle Cases
                case.age = age_range[MID_VAL]
                case.out = calc_out(case)
                out.write(str(case))
                # Upper Edges + Upper Corner Case
                case.age = age_range[R_BOUND]
                case.out = calc_out(case)
                out.write(str(case))

        case = copy(base_case)

        # TABLE: Total Cholesterol
        # points_sex_cho_age
        for sex in test_sex:
            case.sex = sex
            # Lower Corner Case
            case.cho = test_cho[0][L_BOUND]
            case.age = test_age_5[0][L_BOUND]
            case.out = calc_out(case)
            out.write(str(case))
            for cho_range in test_cho:
                for age_range in test_age_5:
                    # Middle Cases
                    case.cho = cho_range[MID_VAL]
                    case.age = age_range[MID_VAL]
                    case.out = calc_out(case)
                    out.write(str(case))
                    # Upper Edges +  Upper Corner Case
                    case.cho = cho_range[R_BOUND]
                    case.age = age_range[R_BOUND]
                    case.out = calc_out(case)
                    out.write(str(case))

        case = copy(base_case)

        # TABLE: HDL (mg/dl)
        # points_sex_smo_age
        case.hdl = test_hdl[0][L_BOUND]
        case.out = calc_out(case)
        out.write(str(case))
        for hdl in test_hdl:
            # Middle Cases
            case.hdl = hdl[MID_VAL]
            case.out = calc_out(case)
            out.write(str(case))
            # Upper Edges +  Upper Corner Case
            case.hdl = hdl[R_BOUND]
            case.out = calc_out(case)
            out.write(str(case))

        case = copy(base_case)

        # TABLE: Smoking
        # points_sex_smo_age
        # TABLE: Systolic BP (mmHg)
        # points_sex_sbp_med
        for sex in test_sex:
            case.sex = sex
            # Lower Corner Case
            #   Smoking            
            case.age = test_age_5[0][L_BOUND]
            #   Systolic BP     
            case.sbp = test_sbp[0][L_BOUND]
            case.out = calc_out(case)
            out.write(str(case))
            for smo, med in zip(test_smo, test_med):
                for age_range, spb_range in zip(test_age_5, test_sbp):
                    # Middle Cases
                    #   Smoking
                    case.smo = smo
                    case.age = age_range[MID_VAL]
                    #   Systolic BP
                    case.med = med
                    case.sbp = spb_range[MID_VAL]
                    case.out = calc_out(case)
                    out.write(str(case))
                    # Upper Edges + Upper Corner Case
                    #   Smoking
                    case.smo = smo
                    case.age = age_range[R_BOUND]
                    #   Systolic BP
                    case.med = med
                    case.sbp = spb_range[R_BOUND]
                    case.out = calc_out(case)
                    out.write(str(case))

        # Manually add cases to reach missing point/output 
        # totals, after examining test.txt file. Find existing lines 
        # with close output and modify one variable to match 
        # point value.
        # F Missing Output Values:
        '''
        [20,    '11'],
        [21,    '14'],
        [23,    '22'],
        [24,    '27'],
        [25,    '≥30']
        '''
        # M Missing Output Values:
        '''
        [0,     '1'],
        [15,    '20'],
        [17,    '≥30']  # >=17
        '''
    # FEMALE:
        # [20,    '11'],
        # MODIFY: sex:F age:75 cho:105 smo:N hdl:60 sbp:180 med:N out:8
        case = test_case(
            sex='F',
            age=75,
            cho=105,
            smo='Y',
            hdl=60,
            sbp=180,
            med='N',
            out='undef'
        )
        case.out = calc_out(case)
        out.write(str(case))
        # [21,    '14'],
        # MODIFY: sex:F age:75 cho:105 smo:Y hdl:60 sbp:180 med:N out:11
        case = test_case(
            sex='F',
            age=75,
            cho=105,
            smo='N',
            hdl=60,
            sbp=180,
            med='Y',
            out='undef'
        )
        case.out = calc_out(case)
        out.write(str(case))
        # [23,    '22'],
        # MODIFY: sex:F age:75 cho:105 smo:N hdl:60 sbp:180 med:Y out:14
        case = test_case(
            sex='F',
            age=75,
            cho=105,
            smo='N',
            hdl=40,
            sbp=180,
            med='Y',
            out='undef'
        )
        case.out = calc_out(case)
        out.write(str(case))
        # [24,    '27'],
        # MODIFY: sex:F age:75 cho:105 smo:N hdl:40 sbp:180 med:Y out:22
        case = test_case(
            sex='F',
            age=75,
            cho=105,
            smo='N',
            hdl=10,
            sbp=180,
            med='Y',
            out='undef'
        )
        case.out = calc_out(case)
        out.write(str(case))
        # [25,    '≥30']
        # MODIFY: just set everything to worst case unhealthiest person ever
        case = test_case(
            sex='F',
            age=79,
            cho=300,
            smo='Y',
            hdl=10,
            sbp=300,
            med='Y',
            out='undef'
        )
        case.out = calc_out(case)
        out.write(str(case))
    # MALE:
        # [0,     '1'],
        # MODIFY: sex:M age:39 cho:159 smo:N hdl:60 sbp:100 med:N out:<1
        case = test_case(
            sex='M',
            age=35,
            cho=140,
            smo='N',
            hdl=10,
            sbp=150,
            med='Y',
            out='undef'
        )
        case.out = calc_out(case)
        out.write(str(case))
        # [15,    '20'],
        # MODIFY: sex:M age:75 cho:105 smo:Y hdl:60 sbp:180 med:Y out:25
        case = test_case(
            sex='M',
            age=75,
            cho=105,
            smo='N',
            hdl=10,
            sbp=100,
            med='N',
            out='undef'
        )
        case.out = calc_out(case)
        out.write(str(case))
        # [17,    '≥30']  # >=17
        # MODIFY: just set everything to worst case unhealthiest person ever
        case = test_case(
            sex='M',
            age=79,
            cho=300,
            smo='Y',
            hdl=10,
            sbp=300,
            med='Y',
            out='undef'
        )
        case.out = calc_out(case)
        out.write(str(case))

if __name__ == "__main__":
    main()