#![allow(unused_imports)]

#[get("/")]
pub fn get_list() -> &'static str {
    "pokemon algo"
}