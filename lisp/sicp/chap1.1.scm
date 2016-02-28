;;1.1.1
(+ (* 3
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7)
      6))
;;1.1.2
(define pi 3.14159)
(define radius 10)
(* pi (* radius radius))
;;1.1.3
(define (square x) (* x x))
(square (+ 2 5))
(square (square 3))
(+ (square 3) (square 4))
;;1.1.6
(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))
(define (abs x)
  (cond ((< x 0) (- x))
        (else x)))
(define (abs x)
  (if (< x 0) 
      (- x)
      x))
(abs 1)
(abs -1)

;;homework
;;1.2
(/ (+ 5 
      4 
      (- 2 
         (- 3
            (+ 6
               (/ 4 5)))))
   (* 3
      (- 6 2)
      (- 2 7)))
;;1.3
(define (max a b)
  (if (> a b)
      a
      b))
(max 3 2)
(define (min a b)
  (if (> a b)
      b
      a))
(min 3 2)
(define (max_top2_sum a b c) 
  (+ (max a b)
     (max (min a b) c)))
(max_top2_sum 1 0 3)
;;1.4
(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))
(a-plus-abs-b 1 -2)
;;1.5
(define (p) (p))
(define (test x y)
  (if (= x 0)
      0
      y))
(test 0 (p)) ;;(stack-overflow)

;;1.1.7
(define (average x y)
  (/ (+ x y) 2))

(define (improve guess x)
  (average guess (/ x guess)))

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(sqrt 2)
(sqrt 999)

;;homework
;;1.6
(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))
(new-if (= 2 3) 0 5)
(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))
(sqrt 4) ;;(stack-overflow)
;;1.7
(square (sqrt 0.001))
(square (sqrt 999999))
(define (good-enough? guess x)
  (< (abs (- (improve guess x) 
             guess)) 
     0.001))
(square (sqrt 0.001))
(square (sqrt 999999))
;;1.8
(define (cube x)
  (cube-iter 1.0 x))

(define (cube-iter guess x)
  (if (good-enough-cube? guess x)
      guess
      (cube-iter (improve-cube guess x) x)))

(define (good-enough-cube? guess x)
  (< (abs (- (improve-cube guess x) 
             guess)) 
     0.001))

(define (improve-cube guess x)
  (/ (+ (/ x 
           (square guess))
        (* 2 guess))
     3))

(cube 27)

;;1.1.8

(define (sqrt x)
  (define (improve guess)
    (average guess (/ x guess)))
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))  
  (sqrt-iter 1.0))
(sqrt 9.26)
