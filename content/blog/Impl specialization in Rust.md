---
title: Impl specialization in Rust
date: 2020-04-11
tags:
- programming
- rust
---
Yesterday I learnt about a feature in Rust, currently only available in nightly: [impl specialization](https://github.com/rust-lang/rfcs/pull/1210).

I had to solve the problem highlighted in the following snippet:

``` rust
use std::hash::Hash;

trait Foo {
    fn get_foo(&self) -> String;
}

impl<T: Hash> Foo for T {
    fn get_foo(&self) -> String {
        "foo for hash".to_string()
    }
}

impl Foo for String {
    fn get_foo(&self) -> String {
        "foo for string".to_string()
    }
}

fn main() {
    let bar: String = "bar".to_string();
    println!("{}", bar.get_foo());

    let baz: i32 = 1;
    println!("{}", baz.get_foo());
}
```

Compiling this code gives the below error:

``` shell
» rustup run stable rustc specialization.rs
error[E0119]: conflicting implementations of trait `Foo` for type `std::string::String`:
  --> specialization.rs:13:1
   |
7  | impl<T: Hash> Foo for T {
   | ----------------------- first implementation here
...
13 | impl Foo for String {
   | ^^^^^^^^^^^^^^^^^^^ conflicting implementation for `std::string::String`

error: aborting due to previous error

For more information about this error, try `rustc --explain E0119`.
```

Rust compiler complains that I have two conflicting implementations of the `Foo` trait for the `String` type. In fact, `String` implements `Hash`, so the compiler can\'t decide which implementation to use for `String`.

As recommended, I ran `rustc --explain E0119`, but no solution to the problem was suggested. It took me a while to find a solution: this blog post is mostly of a reminder to myself what the solution is.

The trick is to use [impl specialization](https://github.com/rust-lang/rfcs/pull/1210), currently available only on nightly. The feature allows to specify a \"default\" implementation for a trait, but also to have other implementations for other traits.

Just enable the unstable feature and use `default fn` instead of `fn` for the default trait implementation. My code now looks like this:

``` rust
#![feature(specialization)]
use std::hash::Hash;
trait Foo {
    fn get_foo(&self) -> String;
}

impl<T: Hash> Foo for T {
    default fn get_foo(&self) -> String {
        "foo for hash".to_string()
    }
}

impl Foo for String {
    fn get_foo(&self) -> String {
        "foo for string".to_string()
    }
}

fn main() {
    let bar: String = "bar".to_string();
    println!("{}", bar.get_foo());

    let baz: i32 = 1;
    println!("{}", baz.get_foo());
}
```

Compilation works and the output of the executable is as expected: the specialised implementation is called for `String` and the default implementation is called for `i32`.

``` shell
» rustup run nightly rustc specialization.rs
» ./specialization
foo for string
foo for hash
```
