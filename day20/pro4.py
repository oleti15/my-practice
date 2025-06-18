posts=[
    {"user":"alice","post":"Hai"},
    {"user":"bob","post":"hello"},
    {"user":"alice","post":"Hai"},
    {"user":"bob","post":"hello"},
    {"user":"john","post":"Hai"}
]
post_count={
}
for i in posts:
    if i["user"] in post_count:
        post_count[i["user"]]+=1
    else:
        post_count[i["user"]]=1
print(post_count)
    

    
    

