n= 374159235470172130988938196520880526947952521620932362050308663243595788308583992120881359365258949723819911758198013202644666489247987314025169670926273213367237020188587742716017314320191350666762541039238241984934473188656610615918474673963331992408750047451253205158436452814354564283003696666945950908549197175404580533132142111356931324330631843602412540295482841975783884766801266552337129105407869020730226041538750535628619717708838029286366761470986056335230171148734027536820544543251801093230809186222940806718221638845816521738601843083746103374974120575519418797642878012234163709518203946599836959811
low=1
high=n
while low < high:
	low+=1
	mid = n%low
	print (low)
	if mid == 0:
		print (mid)
		
		break
q = n / low
print(type(low))
print(type(n))
print(type(q))
print(q)
