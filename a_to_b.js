a = {
    '小明': {
        '性别': '男',
        '成绩': {
            '2015': 90,
            '2016': 85
        }
    },
    '小红': {
        '性别': '女',
        '成绩': {
            '2015': 80,
            '2016': 90
        }
    }
}

b = {
    '2015':{
        '小明':{
            '性别': '男',
            '成绩': 90
        },
        '小红':{
            '性别': '女',
            '成绩': 80
        }
    },
    '2016':{
        '小明':{
            '性别': '男',
            '成绩': 85
        },
        '小红':{
            '性别': '女',
            '成绩': 90
        }
    }
}

b = {}
for (var k in a){
    score = a[k]['成绩']
    for (var s in score){
        b[s][k] = a[k]
        b[s][k]['成绩'] = score[s]
    }
}