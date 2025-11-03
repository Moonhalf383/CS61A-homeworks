(define (ascending? s)
    (if (or (null? s) (null? (cdr s))) #t (if (<= (car s) (car(cdr s))) (ascending? (cdr s)) #f))
  ) 

(define (my-filter pred s) 
    (if (null? s) () (if (pred (car s)) (cons (car s) (my-filter pred (cdr s))) (my-filter pred (cdr s))))
  )

(define (interleave lst1 lst2) 
  (if (null? lst1) lst2 (if (null? lst2) lst1 (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2))))))
  )

(define (no-repeats s) 
  (if (or (null? s) (null? (cdr s))) s (cons (car s) (my-filter (lambda (x) (not (= (car s) x))) (no-repeats (cdr s)))))
  )
