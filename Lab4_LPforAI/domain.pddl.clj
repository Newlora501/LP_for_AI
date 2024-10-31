(define (domain move-agent)
  (:requirements :strips)
  (:predicates 
    (at ?a) ;; положение агента
  )
  (:action move
    :parameters (?from ?to)
    :precondition (at ?from)
    :effect (and 
      (not (at ?from))
      (at ?to)
    )
  )
)
