### 1. 브랜치란?
commit 1 -> commit 2 -> commit 3
이후부터는 버전을 나누어서 작업해야 될 수 있다. (ex. 유료버전, 무료버전) 하지만 현재 상태로는 불가능하다.

이때 **브랜치**라는 개념을 사용한다. branch의 한글 뜻은 '나뭇가지'로, 나뭇가지가 여기저기 뻗어나가듯이 코드 관리 흐름을 여기저기 뻗어나갈 수 있게 하는 요소이다.

---

### 2. 브랜치 기본 명령어

무료 버전과 유료 버전을 나누어서 작업하기 위해 premium이라는 브랜치를 만든다고 가정해보겠다.

**브랜치 만들기**
```bash

git branch premium

# premium이라는 브랜치를 만들어냄.
```

**다른 브랜치로 이동**
```bash

git checkout premium

# premium 브랜치로 이동
```

이동한 브랜치에서 파일을 수정하고 작업한 후 commit하면 main 브랜치에는 반영이 되지 않고 새로운 브랜치에서만 반영이 된다.

**브랜치 상태 조회**
```bash

git branch

# 출력결과
# * main
# premium
```
\* : 현재 내가 있는 브랜치를 나타낸다.

**브랜치 삭제**
```bash

git branch -d premium

# premium 브랜치 삭제
```

**브랜치 생성과 동시에 이동**
```bash

git checkout -b premium

# premium 브랜치를 만들고 premium 브랜치로 이동
```

**다른 브랜치의 커밋 내용 가져오기 (merge)**
```bash

git merge premium

# premium에서 commit한 내용을 main에 가져옴.
```

**실행 과정 :**

1. git merge premium 실행
2. 커밋 메시지를 입력하는 텍스트 에디터가 뜸
3. 커밋 메시지 입력 후 :wq (저장 후 나가기)

---

### 3. Merge Conflict

main, sub 두개의 브랜치가 있고 hello.py라는 파일이 있을 때:

**main 브랜치:**
```python

def hello_world():
	print(hello)
```

**sub 브랜치:**
```python

def hello_korea():
	print(hello)
```

**각 브랜치에서 따로 commit한 후 merge를 시도하면:**
```bash

git merge sub
# Conflict (content) : Merge conflict in hello.py
```

conflit가 발생하는 이유

def hello_world( ):
\------------------------
def hello_korea( ) :

Git 입장에서는 둘 중 뭘로 병합해야 될지 혼란이 생긴다.

**해결 방법 1 : 직접 수정**
 
1. 컨플릭트가 발생한 파일을 연다
2. 머지의 결과가 되었으면 하는 모습대로 코드를 수정
```python
def hello_everyone():
	print(hello)
```
이렇게 통일할 수도 있다.

**해결 방법 2 : merge 취소**
```bash
git merge --abort
# 머지를 시도하기 이전의 모습으로 돌아간다.
```

**여러 파일에서 merge conflict가 발생한다면?**

**방법 1** : 파일 하나씩 conflict를 해결하고, git add로 하나씩 staging area에 올린 후 커밋 (중간중간에 git status로 현재 상태 확인하면서)

**방법 2** : 모든 파일의 conflict를 다 해결하고, git add . 로 한번에 staging area에 올린 후 커밋

💡git status를 사용하면 conflict가 발생한 파일들의 목록을 볼 수 있다.

---

### 4. Remote Repository의 브랜치

Github에서 리모트 레포지토리를 만들고, 로컬 레포지토리의 내용을 보내기 위한 커맨드 : 
```bash
git remote add origin https://github.com/mandoo1015/Math_Box.git
git push -u origin main
```

**리모트 레포지토리 등록**

```bash
git remote add origin <repository_url>.git
```

| 키워드 | 설명 |
| :---: | --- |
| remote | 리모트 레포지토리에 관한 작업을 할 때 쓰는 커맨드 |
| add | 새로운 리모트 레포지토리를 등록 |
| origin | 해당 URL을 origin이라는 이름으로 등록 |

💡 **origin이라고 하는 이유** : git에서는 리모트 레포지토리를 최초로 추가할 때 origin이라는 이름으로 가리키는 것이 관례화 되어있다.


**로컬에서 리모트로 push**

``` bash
git push -u origin main
```

-u는 --set-upstream 옵션의 약자로, 로컬 레포지토리의 main 브랜치가 origin의 main 브랜치를 **tracking**하게 한다.

**Tracking이란?** 로컬 레포지토리의 한 브랜치가 리모트 레포지토리의 한 브랜치와 연결되어 그것을 계속 바라보는 상태가 되는 것이다. 이렇게 맺어진 연결 상태를 **tracking connection**이라고 한다.

**tracking connection의 장점 :**

1. git push만 써도 자동으로 리모트 레포지토리의 main을 대상으로 동작
2. git pull도 마찬가지로 리모트 레포지토리의 main을 대상으로 동작

💡만약 -u 옵션을 주지 않았다면 git push origin main:main 이런 식으로 적어줘야 한다. (앞의 main은 로컬, 뒤의 main은 리모트)

**브랜치 구별하기**
커밋 히스토리에서 : 

1. (main) -> 로컬 레포지토리의 main 브랜치
2. (origin/main) : 리모트 레포지토리의 main 브랜치

**여러 브랜치 push하기**

main 브랜치가 이미 upstream 설정이 되어 있다면, sub 브랜치에도 별도로 설정해줘야 한다.

```bash
git push --set-upstream origin sub
```
---

### 5. HEAD와 branch의 관계 ⭐
branch의 정체 : 코드 관리의 흐름이라고 말했지만, 엄밀히 말하면 브랜치는 커밋을 가리키는 포인터이다.

**(1), (2), (3), (4)의 commit history 가 있을 때 :**
![](https://velog.velcdn.com/images/minseo_dev/post/3ac552bc-bd9f-414a-a5a9-fbe42562041f/image.png)


가리켰던 존재들에 대한 모든 정보들을 담고 있기 때문에 '코드 관리의 흐름'이라는 개념이 성립한다.

**HEAD란?** branch를 가리키는 포인터이다. 
HEAD -> branch -> commit

**(4)에서 sub라는 브랜치 생성 -> git checkout main : **
![](https://velog.velcdn.com/images/minseo_dev/post/9eb859e2-b4db-4de6-a31a-05fd81251321/image.png)

**커밋 : ** 
![](https://velog.velcdn.com/images/minseo_dev/post/1182e9ac-d51a-471b-b194-960ba917f6ed/image.png)


**git merge sub :**
![](https://velog.velcdn.com/images/minseo_dev/post/96bf0426-0cb6-4a04-b103-c3b54ed4befc/image.png)

**git merge 정리** : HEAD가 가리키던 커밋에 다른 브랜치가 가리키던 커밋을 만드는 작업



