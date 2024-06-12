// #![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;

mod controllers;

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![controllers::pokemon_controller::get_list])
}