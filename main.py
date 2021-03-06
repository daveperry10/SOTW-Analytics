
"""
    Call everything from here.  Get the data, initialize a chart grid of any size, and load it up with charts
        Charts:
        -------
        - Code clusters are self-documenting. Caller can:
        - Caller can add a title to the figure
        - Caller can add titles to each component chart in the figure
        - Arguments are almost all function names, grid positions, and key-word args.

        Simulation:
        -----------
        - Call two ways:
            - A/B test to chart two sets of parameters for a single path
            - full Sim to look at
                a. histograms of measured stats at points in time
                b. paths of measured stats
        - Chartable stats:
            navPaths[]
            dfNavPaths[]
            reinvestableCashFlowPaths[]
            servicingFeePaths[]
            dividendPaths[]
            performanceFeePaths[]

"""

import data as s
import charts as c
import matplotlib.pyplot as plt
import time
import pandas as pd
import analytics as a
import payoff as p


def chartsmain():

    d = s.Data()
    d.getFreddieData()
    #d.getMSAData()
    ch = c.Chart(1,2)

    # Schiller Plot
    # c.plotCaseSchiller(d.getCaseSchillerData())

    # Grid of Multiples and Discounts
    # c.gridOfMultiplesAndDiscounts()

    # Grid of IRR by Vintage/Age
    #c.gridOfIRR(d, msa=10900, payoff_status='Defaulted')

    # Histogram of Home Price Appreciation versus Payoff
    #c.histAppreciationVsPayoff(d.getFreddieData(), msa=10900, vintage=1999, payoff_status='Paid Off')

    # ch = c.Chart(2,2, sharey = False, sharex = True, title="Total Appreciation")
    # ch.histGeneric(d.getFreddieData, a.calcTotalAppreciation, (0, 0), vintage=1999, age=4)
    # ch.histGeneric(d.getFreddieData, a.calcTotalAppreciation, (0, 1), vintage=1999, age=7)
    # ch.histGeneric(d.getFreddieData, a.calcTotalAppreciation, (1, 0), vintage=2005, age=4)
    # ch.histGeneric(d.getFreddieData, a.calcTotalAppreciation, (1, 1), vintage=2005, age=7)
    # ch.save()

    # ddd = c.Chart(1,1)
    # d = a.payoffIRR(initialInv, investorShare, apprAnnualized, life, discount)
    # d2 = p.monthlyPayoffTiming(d.getFreddieData(), ddd.axes, yr="all", dollar=False)
    # print(d2)


    # ch1 = c.Chart(4,1, sharey = False, title="Total Appreciation by Multiple Cuts")
    # ch1.setChartFileName("Test1")
    # ch1.histGeneric(d.getFreddieData(), a.calcTotalAppreciation, (0, 0), title='Total Appreciation\n')
    # ch1.histGeneric(d.getFreddieData(), a.calcTotalAppreciation, (1, 0), vintage=2006, title='Total Appreciation\n')
    # ch1.histGeneric(d.getFreddieData(), a.calcTotalAppreciation, (2, 0), payoff_status='Defaulted', vintage=2006, title='Total Appreciation\n')
    # ch1.histGeneric(d.getFreddieData(), a.calcTotalAppreciation, (3, 0), payoff_status='Defaulted', vintage=2006, msa=10900, title='Total Appreciation\n')
    # ch1.save()
    #
    # ch2 = c.Chart(4, 2, sharey=False, title="Annualized SOTW Returns by LTV")
    # ch2.setChartFileName("Test2")
    # ch2.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (0, 0), orig_oltv=(60, 100), age=(2, 10), title='Annualized Payoff\n')
    # ch2.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (1, 0), orig_oltv=(40, 60), age=(2, 10), title='Annualized Payoff\n')
    # ch2.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (2, 0), orig_oltv=(20, 40), age=(2, 10), title='Annualized Payoff\n')
    # ch2.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (3, 0), orig_oltv=(0, 20), age=(2, 10), title='Annualized Payoff\n')
    # ch2.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (0, 1), orig_oltv=(60, 100), age=(0, 10), title='Annualized Payoff\n')
    # ch2.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (1, 1), orig_oltv=(40, 60), age=(0, 10), title='Annualized Payoff\n')
    # ch2.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (2, 1), orig_oltv=(20, 40), age=(0, 10), title='Annualized Payoff\n')
    # ch2.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (3, 1), orig_oltv=(0, 20), age=(0, 10), title='Annualized Payoff\n')
    # ch2.save()

    # ch3 = c.Chart(5, 2, sharey=False, title="Annualized SOTW Returns by Age")
    # ch3.setChartFileName("Test3")
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (0, 0), age=(0, 0), title='Annualized Payoff\n', bins = (-1, 1, .02))
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (1, 0), age=(1, 1), title='Annualized Payoff\n')
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (2, 0), age=(2, 2), title='Annualized Payoff\n')
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (3, 0), age=(3, 3), title='Annualized Payoff\n')
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (4, 0), age=(4, 4), title='Annualized Payoff\n')
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (0, 1), age=(5, 5), title='Annualized Payoff\n')
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (1, 1), age=(6, 6), title='Annualized Payoff\n')
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (2, 1), age=(7, 7), title='Annualized Payoff\n')
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (3, 1), age=(8, 8), title='Annualized Payoff\n')
    # ch3.histGeneric(d.getFreddieData(), a.calcAnnualizedPayoff, (4, 1), age=(9, 10), title='Annualized Payoff\n')
    # ch3.save()

    # ch4 = c.Chart(2,1, sharey=False, title="testAge")
    # ch4.setChartFileName("testAge")
    # ch4.ageGeneric(d.getFreddieData(), (0, 0), pct=True, title='Annualized Payoff\n', vintage=2006)
    # ch4.ageGeneric(d.getFreddieData(), (0, 0), pct=True, byyear=True, title='Default Curve\n', payoff_status='Defaulted', msa = 10900)
    # ch4.ageGeneric(d.getFreddieData(), (0, 0), pct=True, byyear=True, title='Default Curve\n', payoff_status='Defaulted')
    # ch4.ageGeneric(d.getFreddieData(), (2, 0), pct=True, byyear=True, title='Default Curve\n', payoff_status='Defaulted', vintage=2006, msa = 10900)
    # ch4.ageGeneric(d.getFreddieData(), (3, 0), pct=True, byyear=True, title='Default Curve\n', payoff_status='Defaulted', vintage=2006)
    # ch4.save()

    ch5 = c.Chart(2,1, sharex=False, sharey=False)
    ch5.setChartFileName("test kwarg")
    ch5.setTitle("testPivot")
    ch5.pivotGeneric(d.getFreddieData(), (0, 0), age=(2, 10), rows='age', values='ret', vintage=2006, title="Returns by Age")
    ch5.pivotGeneric(d.getFreddieData(), (1, 0), rows='vintage', values='ret', title="Returns by Vintage")
    ch5.save()

    return

from simulation import MeanRevertingProcess, Asset, Account, Simulation

def simABTest(dictA, dictB):
    """
    Show Various Sim Results for two simulation runs with one or more parameter changed on
    the second run.
    *** Charts are on the same axis ***
    Notes:  Trials must be 1.
    :return:
    """
    chart = c.Chart(3,1, sharex=True, sharey=False, title="Sim: A/B Test", bottom=.21, top=.935)

    sim_A = Simulation(**dictA)
    sim_A.simulate()
    chart.chartBasic(sim_A.simresults.totalInvestorValue,(0,1), color='cadetblue', linestyle='-')
    chart.chartBasic(sim_A.simresults.residualCashFlow, (1, 1), legend=True, color='cadetblue', linestyle='-')

    sim_B = Simulation(**dictB)
    sim_B.simulate()

    chart.chartBasic(sim_B.simresults.totalInvestorValue,(0,1), color='brown', linestyle='-', title='Total Investor Value')
    chart.chartBasic(sim_B.simresults.residualCashFlow, (1, 1), title="Cash Flow Paths", legend=True, color='brown', linestyle='-')

    """ PRICE INPUTS """
    chart.chartBasic(sim_A.process.pricePaths, (2, 1), legend=False, color='cadetblue', linestyle='-')
    chart.chartBasic(sim_B.process.pricePaths, (2, 1), title="Price Path", legend=False, color='brown', linestyle='-')

    sim_A.fillTextBox(chart, 0.135, 0.12)
    sim_B.fillTextBox(chart, 0.135, 0.05)

    plt.show()

def simMultiplePaths(**kwargs):
    sim = Simulation(**kwargs)
    sim.simulate()
    sim.describe([40])
    sim.histogram(40, [sim.simresults.totalInvestorValue, sim.simresults.totalFee])
    plt.show()

def simOnePath(**kwargs):
    sim = Simulation(**kwargs)
    sim.simulate()
    sim.chartAllSimResults()
    sim.describe([40])
    #sim.chartNavPaths()
    plt.show()

def simRisk(**kwargs):
    sim = Simulation(**kwargs)
    sim.risk()

"""  TOP-LEVEL CALLERS:

DEFAULTS:

Asset:      initialInv=0.1, investorShare=0.35, discount=0.1, oltv=0.8, assetLife=40
Account:    ramp=[1e6], servicingFee=0.02, performanceFee=0.1, performanceHurdle=0.1, frequency=4, dividend=0.08, flatDiv=True, reinvest=True
Process:    trials=1, processLife=41, growthRate=.05/4, lam=.25, sig=10, seed=0

prepayFile="C:/Users/Dave/Documents/Sum/Analytics/Data/prepay-chris-cpr-q.csv"
defaultFile="C:/Users/Dave/Documents/Sum/Analytics/Data/default-0-cdr-q.csv"
"""

""" SQL DB Charting """
#chartsmain()

""" Single path: A-B Test  """
#simABTest(dict(seed=1), dict(seed=5))

""" Single Path: 5-Chart Performance"""
#simOnePath(seed=2, prepayFile='C:/Users/Dave/Documents/Sum/Analytics/Data/prepay-100psa-q.csv')

""" Multiple Paths:  Trial Stats and Histograms"""
#simMultiplePaths(seed=2, prepayFile='C:/Users/Dave/Documents/Sum/Analytics/Data/prepay-100psa-q.csv')

""" Multiple Paths:  Risk Run"""
simRisk(seed=3, trials=100, growthRate=.055)
