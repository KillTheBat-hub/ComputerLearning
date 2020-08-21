;1.1
;just type and print

;1.2
(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 3)))))
   (* 3 (- 6 2) (- 2 7)))

;1.3
(define (larger-two  x y z)
  (cond ((and (<= x y)(<= x z))
         (sum-squares y z))
        ((and (<= y x)(<= y z))
         (sum-squares x z))
        (else (sum-squares x y))))
(define (sum-squares x y)
  (+ (square x)(square y)))
(define (square x)
  (* x x))

(larger-two -2 3 -2)

;1.4
(define (a-plus-abs-b a b)
   ((if (> b 0)+ -) a b))
;allows evaluations whose operators are compound expressions

;1.5
#| 
normal-evaluation: from the left to the right, strictly following the order
applicative-evaluation: internal reduction applied first, so each segment must be 'no error'
|#

(define (p) (p))
(define (test x y)
  (if (= x 0)
      0
      y))
(test 0 (p))

;if interpreter uses normal-evaluation, 0; if using applicative-evaluation, interpreter will report an error or running quite slowly.
;check 'Macro stepper' button, interal reduction are applied first. So scheme uses applicative-evaluation.

;1.6
(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))
(define (square-root G x)
  (new-if (good-enough? G x)
          G
          (square-root (improve G x) x)))
(define (good-enough? G x)
  (< (abs(- (/ x G) G)) 0.01))
(define (improve G x)
  (/ (+ G (/ x G)) 2))
(define (abs x)
  (if (> x 0)
      x
      (- x)))
(square-root 1.0 16)

;???operate pretty slowly --> calculate the complexity O(?)
;or write it as following:

(define (average x y)
  (/ (+ x y) 2))
(define (sqrt G x)
  (cond ((< (abs(- (/ x G) G)) 0.0001)
        G)
        (else (sqrt (average G (/ x G)) x))))
(sqrt 1.0 16)
;much faster

;1.7
;the lower limit-0.0009765625; can't calculate smaller square roots. the upper limit-12741635492638498.0, 1.2741635492638497e+016，e+017,...
(define (sqrt G x)
  (if (santisfied G x)
      G
      (sqrt (improve G x) x)))
(define (good-enough? G x)
  (< (abs(- (/ x G) G)) 0.001))
(define (improve G x)
  (/(+ G (/ x G))2))
(define (abs x)
  (if (> x 0)
      x
      (- x)))
(define (santisfied G x)
   (< (abs(- (improve G x) G)) 0.01))  
(sqrt 1.0 1623492750272650712059700240750012)
;running pretty faster and without overflowing, but why???

;1.8
(define (cube-roots y x)
  (if (good-enough? y x)
      y
      (cube-roots (improve y x) x)))
(define (measure-y y x)
  (/ (+ (/ x (* y y)) (* 2 y)) 3))
(define (good-enough? y x)
  (< (abs(- (measure-y y x) y)) 0.001))
(define (improve y x)
  (/(+ y (measure-y y x))2))
(define (abs x)
  (if (> x 0)
      x
      (- x)))
(cube-roots 1.0 64)

;1.9
;recursive, iterative

;1.10
;Ackermann's function
(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        (else (A (- x 1)
                 (A x (- y 1))))))
;(A 1 10)=(A 2 4)=(A 3 3)=0
;(f n)=2n, (g n)=0, (h n)=0

