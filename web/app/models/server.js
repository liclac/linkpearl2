import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  slug: DS.attr('string'),

  characters: DS.hasMany('character'),

  population: DS.attr('number'),
});
