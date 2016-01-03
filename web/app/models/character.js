import Ember from 'ember';
import DS from 'ember-data';

export default DS.Model.extend({
  lodestone_id: DS.attr('number'),
  // user

  server: DS.belongsTo('server', { async: true }),
  first_name: DS.attr('string'),
  last_name: DS.attr('string'),
  title: DS.belongsTo('title', { async: true }),

  race: DS.belongsTo('race', { async: false }),
  clan: DS.attr('number'),
  gender: DS.attr('number'),

  // gc
  gc_rank: DS.attr('number'),
  // fc

  // jobs
  levels: DS.hasMany('level', { async: true }),
  // minions
  // mounts

  clan_name: Ember.computed('race', 'clan', function() {
    return this.get('race.clan_' + this.get('clan'));
  }),
});
