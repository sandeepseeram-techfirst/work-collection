package com.codecademy.ccapplication;

import java.util.List;
import java.lang.Iterable;
import java.util.Date;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;

@RestController
@RequestMapping("/superHeroes")
public class SuperHeroController {

  private final SuperHeroRepository superHeroRepository;
  private final SuperReportRepository superReportRepository;

  public SuperHeroController(SuperHeroRepository superHeroRepository, SuperReportRepository superReportRepository) {
    this.superHeroRepository = superHeroRepository;
    this.superReportRepository = superReportRepository;
  }

@GetMapping()
	public Iterable<SuperHero> getSuperHeros() {
    Iterable<SuperHero> superHeroes = superHeroRepository.findAll();
    return superHeroes;
	}

@GetMapping("/heroReport")
public Iterable<SuperReport> getHeroReport() {
  Iterable<SuperReport> superReport = superReportRepository.findAll();
  return superReport;
}

@PostMapping("/addNew")
public String createNewSuperHero(@RequestParam String firstName, @RequestParam String lastName, @RequestParam String superPower) {
  SuperHero newSuperHero = new SuperHero(firstName, lastName, superPower);
  superHeroRepository.save(newSuperHero);
  return "New Super Hero successfully added!";
}
}