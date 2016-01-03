import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  slug: DS.attr('string'),
  clan_1: DS.attr('string'),
  clan_2: DS.attr('string'),
});
