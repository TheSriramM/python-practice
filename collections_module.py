from collections import namedtuple, OrderedDict, defaultdict, Counter, deque

def named_tuple():
    # Named Tuple - For easy accessing of elements
    point = namedtuple("Point", ["x", "y"]) 
    p = point(1, 2)
    print(p.x)

def ordered_dicts():
    # Ordered Dicts - When iterating through a dictionary the ordered list iterates through the order that the elements were inserted
    brands = OrderedDict()
    brands["Hilux"] = "Toyota"
    brands["Ranger"] = "Ford"
    brands["Amarok"] = "Volkswagen"
    for item in brands:
        print(item)

def default_dict():
    # Default Dicts - Don't Raise a key error when trying to access a key that's not in the dict
    # When you access a value that doesn't exist in a default dict, you get zero
    default = defaultdict(int)
    for char in "ABBCABBCABBC":
        default[char] += 1
    print(default)
    # Trying the same with a normal dictionary
    # Won't work because you have to define the key first (you can't directly add one to a key value when it doesn't exist)

def counter_method():
    # Incredibly useful function!
    s_count = Counter("ABCDABCDABCD")
    # for item in s_count:
    #     print(item)

    # There is a most_common function which gets the most commmon kewy and value
    c = Counter({"CPP": 2, "PY": 5, "C": 3})
    print(c.most_common(1))

def double_ended_queue():
    # A queue where you can remove and add stuff from the front and the back
    d = deque("ABCDEF")
    print(d.pop())
    print(d.popleft())
    # There is a rotate function that rotates elements to the other side of the deque
    d.rotate(-2)
    print(d)