arr = [6,5,8,3,0,5]
def merge(arr,l,m,r):
	help = [None]*(r-l+1)
	i = 0
	p1 = l
	cur = m+1
	while p1 <= m and cur <= r:
		if arr[p1] <= arr[cur]:
			help[i] = arr[p1]
			p1 += 1
			i += 1
		else:
			help[i] = arr[cur]
			cur += 1
			i += 1
	while p1 <= m:
		help[i] = arr[p1]
		p1 += 1
		i += 1
	while cur <= r:
		help[i] = arr[cur]
		cur += 1
		i += 1
	for i in range(0,len(help)):
		arr[l+i] = help[i]
		i += 1
def mergeSort(arr,l,r):
	if l == r:
		return
	mid = (l+r)//2
	mergeSort(arr,l,mid)
	mergeSort(arr,mid+1,r)
	merge(arr,l,mid,r)
mergeSort(arr,0,len(arr)-1)
print(arr)

