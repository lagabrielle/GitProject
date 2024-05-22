# 图书信息管理系统包括sid，name，price，summary
import os.path


# 菜单函数
def menu():
    print("*****************************")
    print(f"*" + "图书管理系统".center(22) + "*")
    print(f"* " + "1. 添加新图书信息".ljust(20) + "*")
    print("* 2. 通过图书ID修改图书信息   *")
    print("* 3. 通过图书ID删除图书信息    *")
    print("* 4. 通过书名删除图书信息       *")
    print("* 5. 通过图书ID查询图书信息     *")
    print("* 6. 通过书名查询图书信息       *")
    print("* 7. 显示所有图书信息          *")
    print("* 8. 退出系统                *")
    print("*****************************")
    option = input('请输入您需要的功能编号：')
    return option


# 定义一个保存图书信息的容器
books = []


# books: list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]] = [{"sid": "s09", "name": "《进化论》", "price": 8, "summary": "balabala"},
#          {"sid": "s10", "name": "《艺术史》", "price": 108, "summary": "balabala"},
#          {"sid": "s11", "name": "《生命起源》", "price": 8, "summary": "balabalaa"},
#          {"sid": "s12", "name": "《生命起源》", "price": 8, "summary": "balabalaa"},
#          {"sid": "s14", "name": "《进化论》", "price": 8903, "summary": "balabalaa"}]


# 1.添加图书信息
def addBook(sid, name, price, summary):
    for b in books:
        if b["sid"] == sid:
            print(f"{sid}图书已存在，不能重复添加")
            return "添加失败"
    else:
        book = {"sid": sid, "name": name, "price": price, "summary": summary}
        books.append(book)
        print("添加成功")
        return "添加成功"


def getSid():
    sid = input("请输入图书ID：")
    return sid


def getName():
    name = input("请输入图书名称：")
    return "《" + name + "》"


def getPrice():
    while True:
        price = input("请输入图书价格：")
        if price.isdigit() and int(price) > 0:
            price = int(price)
            return int(price)
        else:
            print("输入有误，请重新输入图书价格")


def getSummary():
    summary = input("请输入图书概要：")
    return summary


# 通过编号修改图书信息函数(modifyBookByID)
def modifyBookByID(sid):
    for b in books:
        if b["sid"] == sid:
            b["name"] = getName()
            b["price"] = getPrice()
            b["summary"] = getSummary()
            print(f"修改成功")
            return "修改成功"
    else:
        print(f"{sid}不存在，无法修改")
        return "无法修改"


# 通过图书ID删除图书函数（deleteBookByID）
def deleteBookByID(sid):
    for b in books:
        if b["sid"] == sid:
            books.remove(b)
            print(f"成功删除编号为{sid}的{b["name"]}图书")
            return "删除成功"
    else:
        print(f"{sid}不存在，无法删除")
        return "删除失败"


# 通过书名删除图书函数(deleteBookByName)
def deleteBookByName(name):
    # 定义一个用来保存被删除数据的列表
    delList = []
    # 遍历，找到要删除的所有同名书名，然后保存起来
    for b in books:
        if b["name"] == name:
            delList.append(b)
    # 开始删除
    if len(delList) > 0:
        for n in delList:
            books.remove(n)
            print(f"成功删除编号为{n["sid"]}的{name}图书")
        else:
            print(f"一共成功删除{len(delList)}本{name}图书")
            del delList
            return "删除成功"
    else:
        print("不存在{name}图书")
        del delList
        return "不存在，删除失败"


# 通过图书ID查询图书函数(queryBookByID)
def queryBookByID(sid):
    for n in books:
        if n["sid"] == sid:
            print(f"sid->{n["sid"].rjust(4, "*")},name->{n["name"]},price->${n["price"]},summary->{n["summary"]}")
            return "查询成功"
    else:
        print(f"不存在{sid}的图书，查询失败")
        return "查询失败"


# 通过书名查询图书函数(queryBookByName)
def queryBookByName(name):
    nameList = []
    for n in books:
        if n["name"] == name:
            nameList.append(n)
    if len(nameList) > 0:
        print(f"{name}书籍共有{len(nameList)}本,信息如下:")
        for n in nameList:
            print(n)
        del nameList
        return "查询成功"
    else:
        print(f"未找到{name}的相关书籍，查询失败！")
        del nameList
        return "查询失败"


# 显示所有图书信息函数(showAllInfo)
def showAllInfo():
    for n in books:
        print(f"{n["sid"].rjust(4, "*")},name->{n["name"]},price->${n["price"]},summary->{n["summary"]}")


# 数据存储函数（save_data)
def save_data():
    with open("db.txt", "w", buffering=-1, encoding="utf-8") as file:
        for item in books:
            bookStr = ""
            print(item)
            for v in item.values():
                bookStr += f"{v}-"
            file.write(bookStr[:-1] + "\n")
    print("文件已保存")

# 数据加载函数（load_data)
def load_data():
    if os.path.exists("db.txt"):
        with open("db.txt", "r", buffering=-1, encoding="utf-8") as file:
            content = file.read()
            content = content.split("\n")
            content.remove("")
            book = {}
            for item in content:
                item = item.split("-")
                # print(item)
                book["sid"] = item[0]
                book["name"] = item[1]
                book["price"] = item[2]
                book["summary"] = item[3]
                books.append(book)
                # print(books)


# 定义管理函数
def bookManager():
    load_data()
    while True:
        option = menu()
        if len(option) == 1 and option in "12345678":
            if option == "1":  # 1.添加图书信息
                addBook(getSid(), getName(), getPrice(), getSummary())
            elif option == "2":  # 2.通过图书ID修改图书信息
                modifyBookByID(getSid())
            elif option == "3":  # 3. 通过图书ID删除图书信息
                deleteBookByID(getSid())
            elif option == "4":  # 4. 通过书名删除图书信息
                deleteBookByName(getName())
            elif option == "5":  #  5. 通过图书ID查询图书信息
                queryBookByID(getSid())
            elif option == "6":  # 6. 通过书名查询图书信息
                queryBookByName(getName())
            elif option == "7":  # 7. 显示所有图书信息
                showAllInfo()
            else:  # 保存并退出
                save_data()
                break
        else:
            print("功能编号不合法，请重新输入！！！")


# 程序入口
if __name__ == "__main__":
    bookManager()
    # load_data()
