import urllib.request
import json

def get_issues_commits():
    github="https://api.github.com/repos/ec505/EE461L-sp19-owl-team/stats/contributors"
    with urllib.request.urlopen(github) as url:
        data = json.loads(url.read().decode())
    list1=[]
    listdata = ["Erick Machado",0]
    list1.insert(0,listdata)
    listdata = ["Connor Fritz",0]
    list1.insert(1,listdata)
    listdata = ["Eric Cen",0]
    list1.insert(2,listdata)
    listdata = ["Hao Yao",0]
    list1.insert(3,listdata)
    listdata = ["Fei He",0]
    list1.insert(4,listdata)
    listdata = ["Chengjing Li",0]
    list1.insert(5,listdata)
    listdata = ["Xiyu Wang",0]
    list1.insert(6,listdata)
    listissue=list1.copy()
    for dict in data:
        name=dict["author"]["login"]
        if name=="ErickMachado95":
            list1[0]=["Erick Machado", dict["total"]];
        elif name == "cdfritz7":
            list1[1] = ["Connor Fritz", dict["total"]];
        elif name == "ec505":
            list1[2] = ["Eric Cen", dict["total"]];
        elif name == "haoyao0131":
            list1[3] = ["Hao Yao", dict["total"]];
        elif name == "feiut":
            list1[4] = ["Fei He", dict["total"]];
        elif name == "FredyLi":
            list1[5] = ["Chengjing Li", dict["total"]];
        elif name == "dldbb":
            list1[6] = ["Xiyu Wang", dict["total"]];
    print(list1)
    github="https://api.github.com/repos/ec505/EE461L-sp19-owl-team/issues"
    with urllib.request.urlopen(github) as url:
        data = json.loads(url.read().decode())
    issue1=issue2=issue3=issue4=issue5=issue6=issue7=0

    for dict in data:
        name=dict["user"]["login"]
        if name=="ErickMachado95":
            issue1=issue1+1
            listissue[0]=["Erick Machado", issue1];
        elif name == "cdfritz7":
            issue2=issue2+1
            listissue[1] = ["Connor Fritz", issue2];
        elif name == "ec505":
            issue3=issue3+1
            listissue[2] = ["Eric Cen", issue3];
        elif name == "haoyao0131":
            issue4=issue4+1
            listissue[3] = ["Hao Yao", issue4];
        elif name == "feiut":
            issue5=issue5+1
            listissue[4] = ["Fei He", issue5];
        elif name == "FredyLi":
            issue6=issue6+1
            listissue[5] = ["Chengjing Li", issue6];
        elif name == "dldbb":
            issue7=issue7+1
            listissue[6] = ["Xiyu Wang", issue7];
    print(listissue)

    names = [f[0] for f in list1]
    commits = [f[1] for f in list1]
    issues = [f[1] for f in listissue]

    return list(zip(names, commits, issues))

