def points(games):
    points=0
    for i in range(len(games)):
        if int(games[i][0])>int(games[i][2]):
            points+=3
        elif int(games[i][0])==int(games[i][2]):
            point+=1
    return(points)

points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])