import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  slug: DS.attr('string'),
  population: DS.attr('number'),
  characters: DS.hasMany('character'),
});
