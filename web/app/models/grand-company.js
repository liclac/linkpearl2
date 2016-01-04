import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  slug: DS.attr('string'),
  short: DS.attr('string'),
  members: DS.attr('number'),
  characters: DS.hasMany('character', { async: true }),
});
