import Ember from 'ember';
import DS from 'ember-data';

export default DS.Model.extend({
  lodestone_id: DS.attr('number'),
  // user

  server: DS.belongsTo('server', { async: false }),
  first_name: DS.attr('string'),
  last_name: DS.attr('string'),
  title: DS.belongsTo('title', { async: true }),

  race: DS.belongsTo('race', { async: false }),
  clan: DS.attr('number'),
  gender: DS.attr('number'),

  gc: DS.belongsTo('grand-company', { async: false }),
  gc_rank: DS.attr('number'),
  fc: DS.belongsTo('free-company', { async: true }),

  levels: DS.hasMany('level', { async: true }),
  minions: DS.hasMany('minion', { async: false }),
  mounts: DS.hasMany('mounts', { async: false }),

  clan_name: Ember.computed('race', 'clan', function() {
    return this.get('race.clan_' + this.get('clan'));
  }),
  gender_name: Ember.computed('gender_name', function() {
    return this.get('gender') === 1 ? "Male" : "Female";
  }),
  gender_icon: Ember.computed('gender_icon', function() {
    return this.get('gender') === 1 ? '\u2642' : '\u2640';
  }),
  gc_rank_obj: Ember.computed('gc.ranks', 'gc_rank', function() {
    if (!this.get('gc.ranks')) {
      return null;
    }
    return this.get('gc.ranks').findBy('rank', this.get('gc_rank'));
  }),
});
