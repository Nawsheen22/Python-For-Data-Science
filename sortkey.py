d={'Apple':150,'Pineapple':40,'Orange':300,'Malta':350}

convert=list(d.keys())
convert.sort()

#printing 
sd={i:d[i] for i in convert}

print (sd)


# sort will be in alphabatic order 