d1=dict(((30,'vinsa'),(27,'thara'),(9,'anju')))
print({x:d1[x] for x in sorted(d1)})
print({x:d1[x] for x in sorted (d1,reverse=True)})
