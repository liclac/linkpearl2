import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  slug: DS.attr('string'),
  short: DS.attr('string'),
  ranks: DS.hasMany('grand-company-rank', { async: false }),
  num_characters: DS.attr('number'),
  characters: DS.hasMany('character', { async: true }),
});
