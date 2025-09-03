# SETS NOTATIONS
### The symbol ∉  indicates that an element is not in a set
### The symbol ∈ indicates that an element is in a set

```
If B = {1, 2, 3, 4}, 
then 2 ∈  B, but 8 ∉ B
```

### The symbol ⊂ denotes 'is a proper subset of'
### The symbol ⊄ denotes 'is not a subset of'

```
If A = {1, 2, 3, 4, 5}, B = {3, 4}, C = {4, 5, 6}
Thus, B ⊂ A and C ⊄ A
```

### The symbol ⊆ (with the equal sign) means "is a subset of" and includes the possibility that the sets are equal, so:
```
{1,2,3} ⊆ {1,2,3} is true.
```
# SETS OPERATIONS
## Union
##### The union (∪) combines all the unique elements from two or more sets into a single set, similar to the logical "OR" ( || ) operation.
```
Examples:
A = {1, 2, 3, 4}
B = {1, 2, 5, 6}
A ∪ B = {1, 2, 3, 4, 5, 6}
```
```
Properties of Union
A ∪ ∅ = A 
A ∪ A = A
If A ⊆ B, then A ∪ B = B
A ∪ B= B ∪ A 
(A ∪ B) ∪ C = A ∪ (B ∪ C)
```
## Intersection
#### The intersection (∩) of two or more sets is the set that contains only the elements that are common to all the sets, similar to the logical "AND" (&) operation.
```
Examples: 
A = {2, 4, 6, 8} 
B = {4, 6, 8, 10}
C = {6, 8, 10}
A ∩ B ∩ C = {6, 8}
```
```
Properties of Intersection
A ∩ ∅ = ∅ 
A ∩ A = A
If A ⊆ B, then A ∩ B = A
A ∩ B = B ∩ A 
(A ∩ B) ∩ C = A ∩ (B ∩ C)
```

## The Principle of Inclusion and Exclusion (PIE)
#### The Principle of Inclusion and Exclusion (PIE) is a fundamental concept in combinatorics and set theory used to count the number of elements in the union of multiple sets below is the case of principle for two sets.
```
∣A ∪ B∣ = ∣A∣ + ∣B∣ − ∣A ∩ B∣
```

## Complement
#### The set complement, denoted as Aᶜ, is a set that contains all the elements that are not in set A, but are in a universal set U. In other words, it includes all the elements from the universal set U that do not belong to set A.
```
Aᶜ= {x | x ∈ U and x ∉ A}

Uᶜ = ∅
∅ᶜ = U
(Aᶜ)ᶜ = A
If  A ⊆ B , then Bᶜ ⊆ Aᶜ
```

## Venn Diagrams
#### A set can be illustrated by a circle with the elements as dots inside, each labelled by a letter or number.
![[Pasted image 20241004112841.png]]
## Power Set
#### The power set contains all subsets of a given set.
```
P(A)={x: x ⊆ A}

If A has N elements, then the number of subsets of A is 2^n
	A = {1, 2}
	P(A) = {∅, {1}, {2}, {1, 2}}
```
