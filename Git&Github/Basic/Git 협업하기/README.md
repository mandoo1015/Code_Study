# Git 협업하기

## `git push` 하기 전에 `git pull`을 먼저
다른 개발자와 협업 시 기준이 되는 건 **리모트 레포지토리**이므로 `git pull` 먼저!
```bash
git pull
# Merge Conflict 발생하면 수정하고
git merge
# 커밋 메시지 수정 후
git push
```

---

## `git fetch`
- 리모트 레포지토리에 있는 브랜치의 내용을 **일단 가져와서 살펴본 후**에 머지하고 싶을 때 사용
- 리모트 레포지토리에 있는 브랜치의 내용과 내가 작성한 코드를 비교해서 **잘못된 부분이 없는지 검토**할 때
```bash
git fetch
git diff
```

💡 `git pull` = `git fetch` + `git merge`

---

## `git blame`
어떤 파일의 특정 코드를 누가 작성했는지 찾아내기 위한 커맨드

---

## `git revert`
커밋한 작업 되돌리기

```bash
git revert [아이디]..[아이디]
# 첫 번째 아이디는 포함하지 않고 뒤의 아이디까지 revert
```
