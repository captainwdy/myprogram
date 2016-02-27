(+ (* 3
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7)
      6))

(define pi 3.14159)
(define radius 10)
(* pi (* radius radius))

(define (square x) (* x x))
(square (+ 2 5))
(square (square 3))
(+ (square 3) (square 4))

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
(test 0 (p))

