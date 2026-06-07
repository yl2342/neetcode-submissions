class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            c_count = [0] * 26

            for c in s:
                c_count[ord(c)-ord("a")] += 1
            
            res[tuple(c_count)].append(s)
        return list(res.values())

# T: O(mn);  S: O(m), or O(m*n) total space output groups are counted


# -----------------------------------------------------------------------------
# QUICK COMPARISON: {}, dict(), defaultdict
# -----------------------------------------------------------------------------
#
#  Feature                  {}          dict()        defaultdict
#  -----------------------  ----------  ------------  --------------------
#  Speed                    Fastest     Slower (call) Same as dict()
#  Key types                Any hash.   Identifier    Any hashable
#  Build from iterable      Comprehend  Yes           Yes
#  Missing key behavior     KeyError    KeyError      Auto-creates default
#  Import required          No          No            collections module
#  Is a dict subclass       —           —             Yes
#
# Rule of thumb:
#   Use {}          → default choice, most idiomatic
#   Use dict()      → building from pairs/zips, or cleaner string-keyed init
#   Use defaultdict → whenever you'd write `if key not in d` or .setdefault()
 
 
# -----------------------------------------------------------------------------
# KEY REQUIREMENTS: Hashable vs Mutable
# -----------------------------------------------------------------------------
#
# A dict key must be HASHABLE. To understand why, here's what happens
# under the hood when you do d[key] = value:
#
#   1. Python calls hash(key) → gets an integer fingerprint
#   2. That integer determines WHERE in memory the value is stored
#   3. On lookup, hash(key) is called again to find that same slot instantly
#      → This is why dict access is O(1) (constant time)
#
# For this to work reliably, the key's hash must NEVER change after insertion.
# That's where mutability breaks things:
#
#   MUTABLE   = the object's contents can change after creation
#               → hash could change → dict can no longer find the slot
#               → Python refuses to hash these at all
#               NOT allowed: list, dict, set
#
#   IMMUTABLE = the object's contents are frozen at creation
#               → hash is stable forever → safe to use as a key
#               Allowed: int, float, bool, str, tuple*, frozenset, None
#
# * Tuples are immutable, but their CONTENTS must also be immutable:
#   hash((1, 2, 3))   → ok, all elements are immutable
#   hash((1, [2, 3])) → TypeError: contains a mutable list
#
# Quick mental check before using something as a key:
#   "Can I change this object's contents after creating it?"
#     YES (list, dict, set)  → not allowed as a key
#     NO  (str, int, tuple)  → safe to use as a key
 
 
# -----------------------------------------------------------------------------
# ESSENTIAL DICT OPERATIONS
# -----------------------------------------------------------------------------
#
# Assume: d = {"a": 1, "b": 2, "c": 3}
#
# --- Access ---
#   d["a"]              → 1, raises KeyError if missing
#   d.get("a")          → 1, returns None if missing (no KeyError)
#   d.get("z", 0)       → 0, returns given default if missing
#
# --- Insert / Update ---
#   d["d"] = 4          → insert new key
#   d["a"] = 99         → overwrite existing key
#   d.update({"e": 5})  → merge another dict in (mutates d)
#   d.update(f=6)       → also accepts keyword args
#
# --- Remove ---
#   d.pop("a")          → removes key, returns its value; KeyError if missing
#   d.pop("z", None)    → safe remove, returns None if key not found
#   d.popitem()         → removes and returns the last inserted (key, value) pair
#   del d["b"]          → removes key in place; KeyError if missing
#   d.clear()           → empties the entire dict
#
# --- Membership ---
#   "a" in d            → True if key exists (does NOT create the key)
#   "a" not in d        → True if key is absent
#
# --- Views (live — reflect any subsequent changes to d) ---
#   d.keys()            → all keys:   dict_keys(["a", "b", ...])
#   d.values()          → all values: dict_values([1, 2, ...])
#   d.items()           → all pairs:  dict_items([("a", 1), ...])
#
# --- Iteration ---
#   for k in d:           → iterate over keys (most common)
#   for k, v in d.items() → iterate over key-value pairs
#
# --- Safe insert (only if key is absent) ---
#   d.setdefault("a", 0)  → returns existing value if key present,
#                            otherwise inserts 0 and returns it
#
# --- Copy ---
#   d.copy()              → shallow copy (nested objects are still shared)
#   copy.deepcopy(d)      → deep copy, fully independent (import copy first)
#
# --- Merge (Python 3.9+) ---
#   {"a": 1} | {"b": 2}  → new merged dict, right side wins on conflict
#   d |= {"c": 3}         → in-place merge (equivalent to d.update(...))
#
# --- Comprehension ---
#   {k: v**2 for k, v in d.items()}         → transform values
#   {k: v for k, v in d.items() if v > 1}   → filter entries



        
        