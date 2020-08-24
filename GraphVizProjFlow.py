# fsm.py - http://www.graphviz.org/content/fsm

from graphviz import Digraph
import pandas as pd

#f = Digraph('finite_state_machine', filename='fsm.gv')
f = Digraph('G', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')

# f.attr('node', shape='doublecircle')
#f.attr('node', shape='circle')

links_df = pd.read_csv("C:/Users/askli/PycharmProjects/ProjFlowchart/iolinks.csv")

for index, row in links_df.iterrows():
    edgelabel = row['FORMAT'] + ' from ' + row['OWNER']
    f.edge(row['INPUTNAME'],row['OUTPUTNAME'],label=edgelabel)


#

#f.edge('Line_17_History', 'Monthly Peak Forecast', label='SS(B)')
#f.edge('PV_History', 'Monthly Peak Forecast', label='SS(S)')
#f.edge('Event Based \\n DR History', 'Monthly Peak Forecast', label='S($end)')
#f.edge('LR_2', 'LR_6', label='SS(b)')
#f.edge('LR_2', 'LR_5', label='SS(a)')
#f.edge('LR_2', 'LR_4', label='S(A)')
#f.edge('LR_6', 'LR_5', label='S(a)')
#f.edge('LR_7', 'LR_8', label='S(b)')
#f.edge('LR_7', 'LR_5', label='S(a)')
#f.edge('LR_8', 'LR_6', label='S(b)')
#f.edge('LR_8', 'LR_5', label='S(a)')

f.view()
