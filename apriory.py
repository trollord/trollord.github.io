import pandas as pd
import numpy as np
import itertools
dataset = pd.read_csv('data.csv',header=None)
transactions = []
for i in range(0,len(dataset)):
  transactions.append({str(dataset.values[i,j])
  for j in range(0,len(dataset.columns)):
    if str(dataset.values[i,j]) != 'nan'})
      print('Transactions:\n')
for transaction in transactions:
print(transaction)

def init_candidates(transactions):
  candidates = dict()

  for transaction in transactions:
    for item in transaction:
      itemset = set() itemset.add(item)
      itemset = frozenset(itemset)
  if itemset not in candidates:
    candidates[itemset] = 1
  else:
    candidates[itemset] += 1
return candidates

def prune_candidates(candidates,support):
  fp =dict()
  for key in candidates:
    if candidates[key] >= support:
      fp[key] = candidates[key]
  return fp

def get_count(transactions,itemset):
  itemset = set(itemset) count = 0 
  for transaction in transactions:
    if itemset.issubset(transaction):
      count+= 1
  return count

def get_candidates(fp,transactions,fp_length):
  candidates = dict()
  for key1 in fp: 
    for key2 in fp:
      if key2 != key1: 
        itemset1 = set(key1)
        itemset2 =set(key2)
        itemset = itemset1.union(itemset2)
        itemset = frozenset(itemset)
  if itemset not in candidates and len(itemset) == fp_length:
    candidates[itemset] = get_count(transactions,itemset)
  return candidates

def get_itemset_length(candidates):
  itemset_len = 0
  for key in candidates:
    itemset_len = len(key)break
  return itemset_lendef
get_rules(fp):
  rules = []
  for itemset in fp:
    itemset =set(itemset)
    for length in range(1,len(itemset)):
      subsets = set(itertools.combinations(itemset, length))
      for subset in subsets:
        lhs = set(subset)
        rhs = itemset.difference(lhs) 
        rules.append([lhs,rhs])
  return rules

def prune_rules(rules,confidence,transactions):
  fp = []
for rule in rules:
  lhs = rule[0]
  rhs = rule[1]
  lhs_rhs = lhs.union(rhs)
  lhs_count = get_count(transactions,lhs)
  lhs_rhs_count = get_count(transactions,lhs_rhs)
  conf  = lhs_rhs_count/lhs_count
  if conf >= confidence:
    support = lhs_rhs_count/len(transactions)
    fp.append([lhs,rhs,support,conf])
  return fp

def display(candidates,fp,length):
  print()
  print("****** {}-Frequent Candidates ******".format(length))
  for  key in candidates:
    print(set(key),' : ',candidates[key])
    print()
  print("****** {}-Frequent Itemlist ******".format(length))
  for key in fp:
    print(set(key),' : ',fp[key])
    
def apriori(transactions,support,confidence):
  support = support/100 * len(transactions)
  confidence = confidence/100
  candidates = init_candidates(transactions) 
  old_fp= prune_candidates(candidates,support)
  final_fp = dict() display(candidates,old_fp,1)
  while True:
    new_fp_length = get_itemset_length(candidates) + 1
    candidates = get_candidates(old_fp,transactions,new_fp_length)
    new_fp = prune_candidates(candidates,support)
    display(candidates,new_fp,new_fp_length)
    if len(new_fp)<1:
      final_fp = old_fpbreak
    else:
      old_fp = new_fp
      rules = get_rules(final_fp)
      fp = prune_rules(rules,confidence,transactions)
  return fp
support = float(input('Enter support percentage : ')) 
confidence= float(input('Enter confidence percentage : '))
fp =apriori(transactions,support,confidence)
results = pd.DataFrame(columns=['LHS','RHS','Support','Confidence'])
for rule in fp:
  results.loc[len(results.index)] = rule print(results)
