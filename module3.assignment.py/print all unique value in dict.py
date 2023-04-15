l=[{"v":"s001"},{"v":"s002"},{"vi":"s001"},{"vi":"s005"}]
print("original list:",l)
u_value=set(val for dic in l for val in dic.values())
print("unique values:",u_value)