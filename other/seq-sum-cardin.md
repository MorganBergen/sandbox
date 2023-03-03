# discrete structures

### sequences, summations, & cardinality

**1.  prove that $Q^{+} \cup Z$ is countable.  write the proof like we discussed earlier in class.**

1.  first we will demonstrate that what is given is true by definitions of theorems

-  $Q^{+}$ is the set of positive rational numbers greater than zero.  it can be represented as 

$$Q^{+} := \{ p/q \mid p \in \{0, \mathbb{Z^{+}}\} \land q \in \mathbb{Z^{+}}\}$$

- a rational number is a number that can be expressed as the quotient or fraction $\frac{p}{q}$ of two integers $\mathbb{Z^{+}}$
-  such that the numerator $p$ is a member of integer from $0$ to $\mathbb{Z^{+}}$
-  and such that the non-zero denominator $q$ is a member of the integer class $\mathbb{Z^{+}}$
-  a set that is either finite or has the same cardinality as the set of positive integers is called countable.
-  the set of positive rational numbers 
-  for $Q^{+}$, $p \in \{0, \mathbb{Z^{+}}\}$ and $q \in \mathbb{Z^{+}}$ is infinitely countable by definition because $\mathbb{Z^{+}}$ is infinitely countable, therefore by definition $Q^{+}$ by itself is infinitely countable

-  according to theorem 1:  $A \cup B$ is countable, iff $A$ is countable, and $B$ is countable

2.  next we will show that $Z$ is countable by constructing a bijection between $Z$ and $\mathbb{Z^{+}}$

3.  finally we will show that $Q^{+} \cup Z$ is countable by showing that $Q^{+} \cup Z$ is countable by definition


**2.  what are the values of these sums, where $S = \{1, 3, 5, 7\}$**

a.  $\sum_{j \in S} j = 1 + 3 + 5 + 7 = 16$

b.  $\sum_{j \in S} j^{2} = 1^{2} + 3^{2} + 5^{2} + 7^{2} = 84$

c.  $\sum_{j \in S} \frac{1}{j} = \frac{1}{1} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7} = \frac{120}{105} = \frac{8}{7}$

d.  $\sum_{j \in S} 1 = 4$ (since there are 4 elements in the set `s.size() == 4`)
