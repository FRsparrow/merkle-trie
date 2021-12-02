#merkle-trie
merkle树和字典树结合
##Node
1. 26个孩子(a-z)，一个value(可能为None)
2. NodeFlag对象，存有该node的hash值缓存和标志位dirty；dirty为0时直接读取缓存hash，否则重新计算hash；在node内容或子node内容发生改变时dirty置1
3. 序列化serialize：(孩子node的索引,hash)用","连接，最后加上value(不为None)
4. 哈希hash：对序列化结果进行hash
##Trie
1. 字典树的get、put
2. put时把路径上的所有node的dirty置1
3. prove：对key走过的node：把(hash(node), serialize(key))放入proof_db用于后续验证
##verify_proof
由root_hash从proof中取出根节点，由key得到孩子node的hash，再由hash从proof中取出孩子节点。重复这一过程直至取出叶子结点value