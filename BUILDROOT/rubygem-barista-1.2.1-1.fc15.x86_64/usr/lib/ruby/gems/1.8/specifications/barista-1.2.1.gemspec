# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "barista"
  s.version = "1.2.1"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Darcy Laycock"]
  s.date = "2011-06-01"
  s.description = "Barista provides simple, integrated support for CoffeeScript in Rack and Rails applications.\n\nMuch like Compass does for Sass, It also provides Frameworks (bundleable code which can be shared via Gems).\n\nLastly, it also provides a Rack Application (which can be used to server compiled code), a around_filter-style precompiler (as Rack middleware) and simple helpers for rails and Haml.\n\nFor more details, please see the the README file bundled with it."
  s.email = "sutto@sutto.net"
  s.extra_rdoc_files = ["LICENSE", "README.md"]
  s.files = ["LICENSE", "README.md"]
  s.homepage = "http://github.com/Sutto/barista"
  s.require_paths = ["lib"]
  s.rubygems_version = "1.7.2"
  s.summary = "Simple, transparent coffeescript integration for Rails and Rack applications."

  if s.respond_to? :specification_version then
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<coffee-script>, ["~> 2.2"])
      s.add_development_dependency(%q<jeweler>, ["~> 1.0"])
      s.add_development_dependency(%q<rspec>, ["~> 2.1"])
      s.add_development_dependency(%q<rr>, ["~> 1.0"])
    else
      s.add_dependency(%q<coffee-script>, ["~> 2.2"])
      s.add_dependency(%q<jeweler>, ["~> 1.0"])
      s.add_dependency(%q<rspec>, ["~> 2.1"])
      s.add_dependency(%q<rr>, ["~> 1.0"])
    end
  else
    s.add_dependency(%q<coffee-script>, ["~> 2.2"])
    s.add_dependency(%q<jeweler>, ["~> 1.0"])
    s.add_dependency(%q<rspec>, ["~> 2.1"])
    s.add_dependency(%q<rr>, ["~> 1.0"])
  end
end
