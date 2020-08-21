### Elements of Programming  

- primitive expressions  
- means of combination: compound elements built from simple ones   
- means of abstraction: compound elements be named and manipulated as units  

### Define  
      #lang sicp  
      ;define  
      (define A (+ 5 5))  
存储`name-object`对的内存称为`environment`

#### procedure defination 

基本格式 `(define (symbol variable-可以是多个) (expression))`    
syntanctic sugar, 实际上内部格式是 `(define symbol(lambda(variable)) (expression))`     


    ;square function
    (define (square x)
     (* x x)) 
    (define (average x y)
      (/ (+ x y) 2))
    (define (mean-square x y)
      (average (square x)(square y)))

    (mean-square 3 2)
    
#### difference between define and define-function  

比较以下： 

      (define (A) (+ A A))
      A
      (A)
      (define (B) (+ 1 1))
      B
      (B)
      (define C (+ 1 1))
      C
      (C)
      ;注意重复定义会报错，不能两次定义A，具体见“局域变量”

### cond & if  

`cond`可以多个判断及选择并行, `if`二选一    

      ;absolute-value function 
      
      ;cond
      (define (absolute x)
      (cond ((< x 0)(- x)) ;根据经验负号之后也要空格
            ((> x 0)(x))
            (else (0)))) ;可以<=, 也可以<然后其他情况全概括在else；写三句只是为了展现cond的并行性
      (absolute (- 5))
      
      ;if
      (define (abs x)
        (if (> x 0)
            x
            (- x)))



### Black-Box Abstractions  

将函数“封装”在一个“黑盒”里，不需要知道内部结构就可以使用它；在编写时，可以先用一个名称表示某种处理，写完主主体函数，然后再写每一步的函数。  
初学阶段可以使用`tree expression`，如下：  
![image](https://github.com/KillTheBat-hub/functional-programming/blob/master/scheme/learn/MIT%206.001/notes/images/ch1_tree_expression.PNG)


      ;square root function
      ;使用牛顿求解绝对值的方法：在 x,x/G 之间寻找平衡
      (define (sqrt G x)
      (if (good-enough? G x)
            G
            (sqrt (improve G x) x)))
      (define (good-enough? G x)
      (< (abs(- G (/ x G))) 0.001)) ;abs函数已经define过了
      (define (improve G x)
        (average G (/ x G))) ;average函数也已经define过了

      (sqrt 1 16) ;G=1,x=16,从1开始迭代找到16的平方根

      ;指定初始值为1
      (define (square-root x)
        (sqrt 1.0 x))

      (square-root 16)

#### block structure  
函数里的变量都有其作用域`scope`，作用域仅限于某个语句的为`bound variable`，非`bound`的变量称为`free`或`global`。变量在其`scope`内可以随意改名，只要保持前后一致即可，不在乎命名为x还是y。    
使用`block structure`的三点好处：
- 将大段代码分割为相对独立的小段  
- 清晰凸显每个变量的作用域  
- 一个`block`里已使用过的函数名，可以在`block`外重新使用，定义为不同的`expression`并互不干扰  

使用`block structure`改写`square root function`，主体函数为首尾、中间函数夹中间的“夹心”构造:  

      ;完整代码
      (define (sqrt x)
        (define (good-enough? G)
            (< (abs(- G (/ x G))) 0.001))
        (define (improve G)
            (average G (/ x G)))
        (define (abs x)
          (if (> x 0)
              x
              (- x)))
        (define (average x y)
          (* (+ x y) .5))
        (define (sqrt-root G)
          (if (good-enough? G)
              G
              (sqrt-root (improve G))))
        (sqrt-root 1.0))

      (sqrt 16)
      
      ;试验一下定义新的abs可正常运行
      (define (abs x y)
        (/ (+ y x) 2))
      (abs 1 2)
 
 tips：先分开写，主要是完成函数而不必考虑分割、封装；等到写完一“块”再将全局变量提出，可有效避免忘记命名变量，造成迷惑。

### Recursive Process
The definition of procedure refers to the procedure itself, either directly or indirectly.   

#### linear iterative & recursive procedure

| Iteration | recursion |
| ---| --- |
| 像矩形 | 像钟型 |
| 没有推后执行（deferred）的操作 | 有推后执行的操作，因此“越堆越长” |
| 空间复杂度固定，一般就是变量的个数 | 空间复杂度与主变量成正比 |
| 掐掉一部分步骤不影响执行 | 掐掉一部分步骤（比如中间最长的几行）不能执行-缺少了部分推后执行的信息 |  

iteration process of 6!:  
![image](https://github.com/KillTheBat-hub/functional-programming/blob/master/scheme/learn/MIT%206.001/notes/images/ch1_iterative.PNG)    
时间复杂度O(x)-所需时间随着x+1而+1/linear，空间复杂度O(1)-无推后执行   

recursion process of 6!:  
![image](https://github.com/KillTheBat-hub/functional-programming/blob/master/scheme/learn/MIT%206.001/notes/images/ch1_recursive.PNG)
时间复杂度O(x)-所需时间随x+1而+2/linear，空间复杂度O(x)-推后执行步骤数=x    
几组代码体会iteration和recursion：  

      ; 1.x+y
      #iteration
      (define (+ x y)
        (if (= x 0)
            (+ x y)
            (+ (- x 1) (+ y 1))))
      ;recursion
       (define (+ x y)
        (if (= x 0)
            (+ x y)
            (+ 1 (+ (- x 1) y))))
       
       ; 2.factorial
       ;iteration
       (define (factorial x)
         (if (= x 1)
             1
             (* x (factorial (- x 1)))))
       ;recursion
       (define (factorial n)
         (define (f product counter max-counter)
           (if (> counter max-counter)
             product
             (f (* product counter)
                        (+ counter 1)
                        max-counter)))
         (f 1 1 n))
 
*scheme语言`tail-recursive`，不需要for和while就能构建循环  

#### tree recursion



          




