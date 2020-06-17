

members = [
           ("name1", "phone1", "email1"),
           ("namex", "phone1", "emailx"),
           ("namez", "phonez", "emailz"),
           ("namey", "phoney", "emailx"),
]

## iterative impl
from collections import defaultdict

clusters = defaultdict(list)

def is_attr_match(c_mem):
  for index, cluster in clusters.items():
    for each_mem in cluster:
      each_mem = each_mem[0]
      if each_mem[0]==c_mem[0] or each_mem[1]==c_mem[1] or each_mem[2]==c_mem[2]:
        return True, index
  return False, None

group = 0

for idx, member in enumerate(members):
  current_member_attrs = member
  if idx == 0:
    clusters[group].append( (current_member_attrs,idx) )
  else:
    status, group_found = is_attr_match(current_member_attrs)
    if status:
      clusters[group_found].append( (current_member_attrs,idx) )
    else:
      group += 1
      clusters[group].append( (current_member_attrs,idx) )

list({ k: [o[-1] for o in v] for k,v in clusters.items() }.values())
