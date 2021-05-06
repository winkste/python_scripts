import pprint

#getting all projects in one dictionary
projects = {}
p = [12345, "name", "descr", "PL", 5678]
projects[p[0]] = p[1:]
p = [1234, "name", "descr", "PL", 568]
projects[p[0]] = p[1:]
print(f'projDict = {pprint.pformat(projects)}')

for i, key in enumerate(projects):
    print(i)
    print(projects[key])

#read excel and store in a python module
#does it make sense to store all data in dictionalies? - later axcess and indexing
#what to look for in the projects identification sheet:
#--- sheet ALL
#filter all "in flight" projects
#--- sheet EMB_SYS
#filter all "emb sys" marked projects
#--- sheet SUMMARY
#calculate the sum of projects:                 Count of projects
#calculate the budget of the projects:          Budget
#calculate the connections to other domains:    Domain Overlap
#--- sheet RD, TD, PD12, PD34, PC
#print RD, TD, PD12, PD34, PC projects



