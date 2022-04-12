# import the financial library
import FinanceCalcs

# create finance objects

simplecalc = FinanceCalcs.SimpleFinanceCalc()
compoundcalc = FinanceCalcs.CompoundFinanceCalc()

compound_args = {'principal': 530100,
                'interest_rate': 4.375,
                'time': 30,
                'periods': 12
                }

house_pmt = compoundcalc.c_pv2pmt(**compound_args)
house_amort = compoundcalc.amort_sched(** house_pmt)
