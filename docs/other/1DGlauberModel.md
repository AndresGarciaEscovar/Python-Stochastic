# Math 527 - Math of Complex Physical Systems

Suggestion, use Visual Studio Code for better markdown support.

## Summary

The "1D Glauber Spin Model" refers to the stochastic process that leads to the
equilibration of a 1-dimensional periodic chain of "atoms" whose spin values can
only take two values "up" (&#8593; = 1) or "down" (&#8595; = -1) and can only 
interact with their nearest neighbors. The equilibrium magnetization will depend
on the value of the magnitude and sing of the coupling, i.e., the interaction 
"constant".

# Initial Conditions
We will assume that all the spins start in the "down" (&#8595; = -1) state, i.e.
the pictorial representation of the lattice is such that:

|Spin Value|&#8595;|&#8595;|...|...|...|&#8595;|
|---------:|:-----:|:-----:|:-:|:-:|:-:|:-----:|
| Site     |   1   |   2   |   |   |   |   n   |

where site $site_{N+1}=1$ and $site_{0}=N$.

## 1D Glauber Spin Model
Fortran 77 code for the Glauber 1D Spin Model.
```fortran
c     1D-GLAUBER MODEL
      implict real*8(a-h, o-x), integer*4 (i-n, z)
      dimension z(1000)
      read(5,*) ial, n, tstop, tkelvin
      call srand(ial)
 111  format(2x, 'rng seed = ', i10)
      write(6, 112) n
 112  format(2x, 'lattice size = ', i10)
      write(6, 113) tstop
 113  format(2x, 'termination criterion = ', id10.4)
      write(6, 114) tkelvin
 114  format(2x, 'value of 2J/kT = ', 1d10.4)
      write(6, 115)
 115  format(6x, 'TIME', 12x, 'DENSITY OF SPINS DOWN')
c     CALCULATE THE MAXIMUM RATE.
      wmax=amax1 (1.0d0-tanh(tkelvin), 1.0d0+tanh(tkelvin))
c     NUMBER OF SPINS DOWN.
      ndown=n
      write(6, 100) (1.0d0*nattempts)/n, (1.0d0*ndown)/n
c     INITIAL ARRAY OF SPINS VALUES, SAY, ALL DOWN.
      do i=1,n
         z(i)=(-1)
      end do
c     PICK A RANDOM NUMBER BETWEEN 0 AND 1; TRANSFORM INTO A LATTICE SITE
 80   x=rand()
      i=jidint(n*x)+1
      nattempts=nattemps+1
c     DESIGNATE NEIGHBORING SITES; IMPOSE PERIODIC BOUNDARY CONDITIONS
      iplus=i+1
      iminus=i-1
      if(i.eq.n) iplus=1
      if(i.eq.1) iminus=n
c     FIND SITE AND NN NEIGHBOR SPIN VALUES => CHOOSE TRANSITION RATE
      if(((z(iminus)+z(i)+z(iplus)).eq.(-3)).or.
    1 ((z(iminus)+z(i)+z(iplus)).eq.(3))) then
         w=(1.0d0-tanh(tkelvin))/wmax
         u=rand()
         if(u.le.w) z(i)=z(i)*(-1)
         goto 90
      end if
      if((z(iminus)*z(iplus)).lt.0) then
         w=1.0d0/wmax
         u=rand()
         if(u.le.w) z(i)=z(i)*(-1)
         goto 90
      end if
      if((z(iminus)*z(iplus)).gt.0).and.
    1 ((z(minus)*z(i).lt.0)) then
         w=(1.0d0+tanh(tkelvin))/wmax
         u=rand()
         if(u.le.w) z(i)=z(i)*(-1)
         goto 90
      end if
 90   continue
c     COUNT THE NUMBER OF SPINS DOWN
      ndown=0
      do i=1,n
         if(z(i).lt.0) ndown =ndown+1 
      end do
c     WRITE DOWN THE RESULT AND CHECK IF THE SIMULATION CAN STOP
      write(6,100) (1.0d0*nattempts)/n, (1.0d0*ndown)/n
      if(((1.0d0*ndown)/n).ge.tstop) goto 80
 100  format(2x,1d14.4,2x,1d14.4)
      stop
      end
```
Notice that the conditions `z(iminus)+z(i)+z(iplus)=3` or 
`z(iminus)+z(i)+z(iplus)=-3` implies that the spin configuration is either 
&#8593;&#8593;&#8593; or &#8595;&#8595;&#8595;; where the middle spins is the 
spin that is attempting to flip.