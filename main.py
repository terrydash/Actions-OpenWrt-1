from parse import compile

f = open('/home/coder/project/docker/Actions-OpenWrt-1/.github/workflows/build-openwrt.yml', 'r')
p = compile('echo "::set-env name={key}::{val}"')
results = []
for lines in f.readlines():
    # print(lines,end='')
    r = p.parse(str(lines).rstrip())
    if r is not None:
        line = f'echo "{r["key"]}={r["val"]}" >> $GITHUB_ENV'
        line=line+"\n\r"
    else:
        line=lines
    results.append(line)
    
f.close()

with open('/home/coder/project/docker/Actions-OpenWrt-1/.github/workflows/build-openwrt2.yml', 'w+') as f:
    f.writelines(results)
