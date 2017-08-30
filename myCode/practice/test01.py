def search_for_links(page, add_to=[]):
    new_links = page.search_for_links()
    add_to.extend(new_links)
    return add_to

def fn(var1, var2=[]):
    print(var2)
    var2.append(var1)
    print(var2)

fn(3)
fn(4)
fn(5)
fn(3)

def fn1(var1, var2=None):
    print(var2)
    if not var2:
        var2=[]
    var2.append(var1)
    print(var2)

fn1(3)
fn1(4)
fn1(5)
fn1(3)


class URLCatcher(object):
    urls = []

    def add_url(self, url):
        self.urls.append(url)   #同上类似问题，urls列表被实例化后，该类所有实例使用相同列表。

class UrlCatcherCorrect(object):
    def __init__(self):
        self.urls = []
    def add_url(self, url):
        self.urls.append(url)

#可变数据类型作为函数定义中的默认参数.在 Python 中，当我们编写这样的函数时，这个列表被实例化为函数定义的一部分。当函数运行时，它并不是每次都被实例化。这意味着，这个函数会一直使用完全一样的列表对象，除非我们提供一个新的对象fn(3, [4]).对于不可变数据类型，比如元组、字符串、整型，是不需要考虑这种情况的。

#可变类型如字典、数组会出现类似问题。a = {'1': "one", '2': 'two'}，b = a，b['3'] = 'three'后，a输出{'1': "one", '2': 'two', '3': 'three'}。所以，列表复制方法为b=a[:],字典复制方法为a.copy()