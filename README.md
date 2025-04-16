# alpha

Experimental Magma and SageMath exact implementation of the alpha function in
the TNFS (tower number field sieve) setting.    

## How to cite this work

   **On the alpha value of polynomials in the tower number field sieve algorithm**,
    _Aurore Guillevic and Shashank Singh_,
	Mathematical Cryptology, Vol 1 No 1 (Feb 2021),
	[open access](https://journals.flvc.org/mathcryptology/issue/view/5910),
    [eprint 2019/885](https://eprint.iacr.org/2019/885).

```
@article{GuillevicSingh21,
  title     = {On the alpha value of polynomials in the Tower Number Field Sieve Algorithm},
  volume    = {1},
  number    = {1},
  journal   = {Mathematical Cryptology},
  author    = {Guillevic, Aurore and Singh, Shashank},
  year      = {2021},
  month     = {Feb.},
  note      = {open access at \url{https://journals.flvc.org/mathcryptology/article/view/125142}},
}
```

The folder [`sage`](./sage/) contains SageMath code and a long 
[README](./sage/README.md) file.
The alpha function is implemented in 
[`sage/tnfs/alpha/alpha_tnfs_2d.py`](./sage/tnfs/alpha/alpha_tnfs_2d.py). 
A root counting function modulo increasing powers of a prime _p_ is implemented in 
[`sage/tnfs/alpha/number_roots_mod_pk.py`](./sage/tnfs/alpha/number_roots_mod_pk.py)
(it corresponds to Appendix B in the preprint).
The folder contains the simulation of the TNFS relation collection, with
polynomial selection.
A large data of pairing-friendly curves and parameter values is given in
[`sage/tnfs/param/testvector_sparseseed.py`](./sage/tnfs/param/testvector_sparseseed.py).    

The folder [`magma`](./magma/) only contains a Magma implementation of alpha in
the TNFS setting.

An implementation of alpha in the NFS setting is available with the software 
[cado-nfs](https://cado-nfs.gitlabpages.inria.fr).

