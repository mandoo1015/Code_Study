# 자유자재 활용을 위한 커맨드 정리

**지금까지 가리켜왔던 커밋들을 기록한 정보를 보고 싶을 때:**
```bash
git reflog
# reflog : reference log
```
💡 git reset을 한다고 지금까지 했던 커밋 히스토리가 삭제되는 건 아니다.


**reset 하기 이전 커밋으로 되돌아가고 싶다면 :**
```bash
git reflog
git reset --hard [커밋 아이디]
```
---

**커밋 히스토리를 그래프 형식으로 출력하고 싶다면:**
```bash
git log --all --graph
```
각 브랜치와의 관계가 잘 드러나도록 그래프 형식으로 출력해준다.

---

**커밋을 깔끔하게 재배치**
```bash
git rebase [브랜치]
# 컨플릭트가 발생했다면 해결 후
git rebase --continue
```

💡 merge와 rebase 언제 사용하는지?
- merge : 두 브랜치를 합쳤다는 정보가 커밋 히스토리에 꼭 남아야하는 경우
- rebase : 커밋 히스토리를 깔끔하게 유지하는 게 더 중요한 경우

---

**어떤 브랜치에서 하던 작업을 아직 커밋하지 않았는데 다른 브랜치로 가야하는 상황 :**
```bash
git stash
```
stack에 저장 -> 가장 먼저 저장한 데이터를 가장 나중에 꺼낼 수 있음

```bash
git stash list # 저장한 내용들 조회
git stash apply [작업 내용의 아이디] # 스택에 있는 내용 조회
git stash drop # 내용 지우기
git stash pop [작업 내용의 아이디]  # 적용한 작업 내용(apply)을 바로 stack에서 없애주는 커맨드 
```
**git stash를 쓰는 다른 상황 : 다른 브랜치에서 잘못 작업하고 있었을 때**

`git stash`로 작업 내용 저장 -> 올바른 브랜치로 가서 `git stash apply`

💡 전달 인자를 안주면 제일 최근의 작업 내용을 적용

---

**자신이 원하는 작업이 들어있는 커밋들만 가져와서 추가하고 싶을 때 :**
```bash
git cherry-pick [커밋아이디]
```
---

**불필요한 커밋 없애고 싶을 때:**
```bash
git reset --mixed # 또는
git reset --soft
# working directory는 그대로

```
