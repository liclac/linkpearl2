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
  // minions
  // mounts

  clan_name: Ember.computed('race', 'clan', function() {
    return this.get('race.clan_' + this.get('clan'));
  }),
});
